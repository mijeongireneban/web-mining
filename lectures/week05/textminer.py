"""

The script includes the following pre-processing steps for text:
- Sentence Splitting
- Term Tokenization
- Ngrams
- POS tagging

The run function includes all 2grams of the form: <ADVERB> <ADJECTIVE>

POS tags list: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
"""

import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk import load


def run(fpath):

    # make a new tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    # read the input
    f = open(fpath)
    text = f.read().strip()
    f.close()

    # split sentences
    sentences = sent_tokenize(text)
    print('NUMBER OF SENTENCES: ', len(sentences))

    adjAfterAdv = []  # holds the adverb-adjective pairs found in the text

    # for each sentence
    for sentence in sentences:

        terms = nltk.word_tokenize(sentence)  # tokenize the sentence
        # do POS tagging on the tokenized sentence
        tagged_terms = tagger.tag(terms)

        for i in range(len(tagged_terms)-1):  # for every tagged term
            term1 = tagged_terms[i]  # current term
            term2 = tagged_terms[i+1]  # following term

            # current term is an adverb, next one is an adjective
            if re.match('RB', term1[1]) and re.match('JJ', term2[1]):
                # add the adverb-adj pair to the list
                adjAfterAdv.append((term1[0], term2[0]))

    return adjAfterAdv


if __name__ == '__main__':
    print(run('input.txt'))
