"""
Number of lines that includes the word
"""


def run(path, word1, word2):
    freq = {}  # new dictionary. Maps each word to each frequency

    # initialize the frequency of the two words to zero.
    freq[word1] = 0
    freq[word2] = 0

    fin = open(path)  # open a connection to the file
    for line in fin:  # read the file line by line
        # lower() converts all the letters in the string to lower-case
        # strip() removes blank space from the start and end of the string
        # split(c) splits the string on the character c and returns a list of the pieces. For example, "A1B1C1D".split('1')" returns [A,B,C,D]
        words = line.lower().strip().split(' ')

        flag1 = False
        flag2 = False
        # use for to go over all the words in the list
        for word in words:  # for each word in the line
            if word == word1:
                # if the word is word1, then increase the count of word1 by
                # freq[word1] = freq[word1]+1
                flag1 = True
            elif word == word2:
                # if the word is word2, then increase the count of word2 by 1
                # freq[word2] = freq[word2]+1
                flag2 = True

        if flag1 == True:
            freq[word1] = freq[word1] + 1
        if flag2 == True:
            freq[word2] = freq[word2] + 1
    fin.close()  # close the connection to the text file

    return freq[word1], freq[word2]


# use the function
print(run('textfile', 'blue', 'yellow'))
print(run('textfile', 'name', 'kate'))
