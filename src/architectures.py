import torch

import numpy as np

from overrides import overrides
from torch.nn.modules.linear import Linear
from torch.nn.modules.rnn import LSTMCell
from allennlp.modules.similarity_functions import SimilarityFunction
from allennlp.common.util import START_SYMBOL, END_SYMBOL
from allennlp.modules import Attention, TextFieldEmbedder, Seq2SeqEncoder
from allennlp.data.vocabulary import Vocabulary
from allennlp.models.encoder_decoders.simple_seq2seq import SimpleSeq2Seq
from allennlp.modules.token_embedders import Embedding
from allennlp.data.tokenizers.token import Token
from allennlp.data.tokenizers.tokenizer import Tokenizer
from allennlp.nn.beam_search import BeamSearch

from typing import Dict, Optional, List, Tuple, Union, Iterable, Any

Labels = List[Any]



class G2PSeq2Seq(SimpleSeq2Seq):
    
    def __init__(self,
                 vocab: Vocabulary,
                 source_embedder: TextFieldEmbedder,
                 encoder: Seq2SeqEncoder,
                 max_decoding_steps: int,
                 attention: Attention = None,
                 attention_function: SimilarityFunction = None,
                 beam_size: int = None,
                 target_namespace: str = "tokens",
                 target_embedding_dim: int = None,
                 scheduled_sampling_ratio: float = 0.) -> None:
        super(SimpleSeq2Seq, self).__init__(vocab)
        self._target_namespace = target_namespace
        self._scheduled_sampling_ratio = scheduled_sampling_ratio

        # We need the start symbol to provide as the input at the first timestep of decoding, and
        # end symbol as a way to indicate the end of the decoded sequence.
        self._start_index = self.vocab.get_token_index(START_SYMBOL, self._target_namespace)
        self._end_index = self.vocab.get_token_index(END_SYMBOL, self._target_namespace)

        # At prediction time, we use a beam search to find the most likely sequence of target tokens.
        beam_size = beam_size or 1
        self._max_decoding_steps = max_decoding_steps
        self._beam_search = BeamSearch(self._end_index, max_steps=max_decoding_steps, beam_size=beam_size)

        # Dense embedding of source vocab tokens.
        self._source_embedder = source_embedder

        # Encodes the sequence of source embeddings into a sequence of hidden states.
        self._encoder = encoder

        num_classes = self.vocab.get_vocab_size(self._target_namespace)

        # Attention mechanism applied to the encoder output for each step.
        if attention:
            if attention_function:
                raise ConfigurationError("You can only specify an attention module or an "
                                         "attention function, but not both.")
            self._attention = attention
        elif attention_function:
            self._attention = LegacyAttention(attention_function)
        else:
            self._attention = None

        # Dense embedding of vocab words in the target space.
        target_embedding_dim = target_embedding_dim or source_embedder.get_output_dim()
        self._target_embedder = Embedding(num_classes, target_embedding_dim)

        # Decoder output dim needs to be the same as the encoder output dim since we initialize the
        # hidden state of the decoder with the final hidden state of the encoder.
        self._encoder_output_dim = self._encoder.get_output_dim()
        self._decoder_output_dim = self._encoder_output_dim

        if self._attention:
            # If using attention, a weighted average over encoder outputs will be concatenated
            # to the previous target embedding to form the input to the decoder at each
            # time step.
            self._decoder_input_dim = self._decoder_output_dim + target_embedding_dim
        else:
            # Otherwise, the input to the decoder is just the previous target embedding.
            self._decoder_input_dim = target_embedding_dim

        # We'll use an LSTM cell as the recurrent cell that produces a hidden state
        # for the decoder at each time step.
        # TODO (pradeep): Do not hardcode decoder cell type.
        self._decoder_cell = LSTMCell(
            self._decoder_input_dim, 
            self._decoder_output_dim,
        )

        # We project the hidden state from the decoder into the output vocabulary space
        # in order to get log probabilities of each target token, at each time step.
        self._output_projection_layer = Linear(self._decoder_output_dim, num_classes)

    @overrides
    def forward(self,  # type: ignore
                source_tokens: Dict[str, torch.LongTensor]) -> Dict[str, torch.Tensor]:
        # pylint: disable=arguments-differ
        state = self._encode(source_tokens)

        output_dict = {}
        state = self._init_decoder_state(state)
        predictions = self._forward_beam_search(state)
        output_dict.update(predictions)

        return output_dict



@Tokenizer.register("whitespace_")
@Tokenizer.register("just_spaces_")
class WhitespaceTokenizer(Tokenizer):
    """
    A `Tokenizer` that assumes you've already done your own tokenization somehow and have
    separated the tokens by spaces.  We just split the input string on whitespace and return the
    resulting list.

    Note that we use `text.split()`, which means that the amount of whitespace between the
    tokens does not matter.  This will never result in spaces being included as tokens.

    Registered as a `Tokenizer` with name "whitespace" and "just_spaces".
    """

    @overrides
    def tokenize(self, text: str) -> List[Token]:
        return [Token(t) for t in text.split()]