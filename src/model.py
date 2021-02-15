import os
import torch

from allennlp.data.dataset_readers.seq2seq import Seq2SeqDatasetReader
from allennlp.data.vocabulary import Vocabulary
from allennlp.data.token_indexers import SingleIdTokenIndexer
from allennlp.data.tokenizers.character_tokenizer import CharacterTokenizer
from allennlp.modules.token_embedders import Embedding
from allennlp.modules.text_field_embedders import BasicTextFieldEmbedder
from allennlp.modules.seq2seq_encoders import StackedSelfAttentionEncoder
from allennlp.modules.attention import DotProductAttention
from allennlp.predictors import SimpleSeq2SeqPredictor
from src.architectures import G2PSeq2Seq, WhitespaceTokenizer



class Russian_G2P:
    
    def __init__(
        self, model_path, LET_EMBEDDING_DIM=256,
        SOU_EMBEDDING_DIM=256, HIDDEN_DIM=256
    ):
        reader = Seq2SeqDatasetReader(
            source_tokenizer=CharacterTokenizer(),
            target_tokenizer=WhitespaceTokenizer(),
            source_token_indexers={'tokens': SingleIdTokenIndexer()},
            target_token_indexers={'tokens': SingleIdTokenIndexer(namespace='target_tokens')}
        )
        # And here's how to reload the model.
        vocab = Vocabulary.from_files(os.path.join(model_path, 'vocabulary'))

        let_embedding = Embedding(
            num_embeddings=vocab.get_vocab_size('tokens'),
            embedding_dim=LET_EMBEDDING_DIM
        )
        source_embedder = BasicTextFieldEmbedder({"tokens": let_embedding})

        encoder = StackedSelfAttentionEncoder(
            input_dim=LET_EMBEDDING_DIM,
            hidden_dim=HIDDEN_DIM,
            projection_dim=128,
            feedforward_hidden_dim=128,
            num_layers=1,
            num_attention_heads=8
        )

        attention = DotProductAttention()

        max_decoding_steps = 40
        model = G2PSeq2Seq(
            vocab, source_embedder, encoder, max_decoding_steps,
            target_embedding_dim=SOU_EMBEDDING_DIM,
            target_namespace='target_tokens',
            attention=attention,
            beam_size=5
        )

        with open(os.path.join(model_path, 'weights.th'), 'rb') as f:
            model.load_state_dict(torch.load(f, map_location=torch.device('cpu')))
        
        self.predictor = SimpleSeq2SeqPredictor(model, reader)

    def predict(self, word):
        return self.predictor.predict(word)['predicted_tokens']
