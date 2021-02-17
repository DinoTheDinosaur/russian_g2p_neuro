# Russian G2P neuro
G2P tool for Russian language with **vosk-model-ru** styled transcriptions, see the available models in https://alphacephei.com/vosk/models. Based on AllenNLP Seq2Seq architecture.
## Installation
Easiest is installed on Python 3.6, works on Python 3.8
### Direct pip installation
```
pip install git+https://github.com/DinoTheDinosaur/russian_g2p_neuro.git
```
### Installation through cloning + setup.py
If some files are not included after installation, then one should try cloning and installing from source
```
git clone https://github.com/DinoTheDinosaur/russian_g2p_neuro.git
cd russian_g2p_neuro/
python setup.py install
```
## Usage
To generate a Kaldi-like dictionary use a command line tool:
```
generate_transcriptions input.txt output.dict
```
This binary can be used for list of words, but also whole texts.
