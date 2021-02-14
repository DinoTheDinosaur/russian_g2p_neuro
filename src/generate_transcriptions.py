import re
import os
import sys

from pathlib import Path
from src.model import Russian_G2P

MODULE_PATH = Path(__file__).parents[1]

g2p = Russian_G2P(MODULE_PATH / 'model')

def write_result_to_file(dictionary, output_filename, sep=' '):
    lines = []
    for word, transcription in dictionary.items():
        lines += [sep.join([word, transcription])]
    with open(output_filename, 'w') as f:
        f.write('\n'.join(lines))

def transcribe_word_list(wordlist):
    result = {}
    for word in wordlist:
        prediction = g2p.predict(word)
        result[word] = ' '.join(prediction)
    return result

def find_words_in_file(filename):
    with open(filename) as f:
        text = f.read().lower()
    words = re.findall(
        '[ёйцукенгшщзхъэждлорпавыфячсмитьбю\-]+',
        text
    )
    words = sorted(list(set(words)))
    return words

if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    wordlist = find_words_in_file(sys.argv[1])
    dictionary = transcribe_word_list(wordlist)
    write_result_to_file(dictionary, output_filename)
