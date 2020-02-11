# Mijeong Ban
# I pledge my honor that I have abided by the Stevens Honor System


def loadLexicon(fname):
    newLex = set()
    lex_conn = open(fname)
    for line in lex_conn:
        newLex.add(line.strip())
    lex_conn.close()

    return newLex


def run(path):
    result = {}
    reviews = []
    last_words = []

    negLex = loadLexicon('negative-words.txt')

    fin = open(path)
    for line in fin:
        line = line.lower().strip()
        reviews.append(line)
        words = line.split(' ')

        for word in words:
            if word in negLex:
                result[word] = 0

        list_of_words = line.split()
        last_word = list_of_words[-1]
        last_words.append(last_word)
    for word in last_words:
        if word in result:
            result[word] += 1

    fin.close()
    return result


if __name__ == "__main__":
    print(run('textfile'))
