import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk import load


def ngrammer(text):
    # tag for every word based on sentence.
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)  # loading a pre-trained model

    # split sentences
    # converts to list of sentences. can do '.' split but not always true coz if i am saying 6.78 it will take as poimt or what if i have a ?
    sentences = sent_tokenize(text)
    print('NUMBER OF SENTENCES: ', len(sentences))

    # holds the adverb-adjective pairs found inthe text(list of 2-grams)
    nounAfterAdj = []

    # for each sentence
    for sentence in sentences:

        # tokenize the sentence (list of all words in sentence) (can do split a t space but not always works so use this)
        terms = nltk.word_tokenize(sentence)

        # do POS tagging on the tokenized sentence
        tagged_terms = tagger.tag(terms)

        for i in range(len(tagged_terms)-1):  # for every tagged term
            term1 = tagged_terms[i]  # current term
            term2 = tagged_terms[i+1]  # following term

        # re.match checks if it starts with same prefix. re.look looks for whole word
            # current term is an adverb, next one is an adjective
            if re.match('JJ', term1[1]) and re.match('NN', term2[1]):
                # add the adverb-adj pair to the list
                nounAfterAdj.append((term1[0].lower(), term2[0].lower()))

    return nounAfterAdj


def process(text1, text2):

    nounAfterAdj1 = ngrammer(text1)
    nounAfterAdj2 = ngrammer(text2)

    print(nounAfterAdj1, nounAfterAdj2)
    count = 0

    for i in nounAfterAdj1:
        for j in nounAfterAdj2:
            if(i[0] == j[0] and i[1] == j[1]):
                count += 1

    return count


if __name__ == '__main__':
    text1 = "I have great food and amazing drinks. The place has great music"
    text2 = "If you like great food, go to place. They have best steak."
    print(process(text1, text2))
