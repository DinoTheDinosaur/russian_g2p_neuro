# Russian G2P neuro
G2P tool for Russian language with **vosk-model-ru** styled transcriptions, see the available models in https://alphacephei.com/vosk/models. Based on AllenNLP Seq2Seq architecture.
## Installation
Easiest is installed on Python 3.6, works on Python 3.8
`pip install git+https://github.com/DinoTheDinosaur/russian_g2p_neuro.git`
## Usage
To generate a Kaldi-like dictionary use a command line tool:
`generate_transcriptions input.txt output.dict`
This binary can be used for list of words, but also whole texts.
