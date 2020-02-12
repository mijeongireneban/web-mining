# Mijeong Ban
import re
from nltk.corpus import stopwords
import requests
from operator import itemgetter


def run(url, w1, w2):

    freq = {}

    result = set()

    stopLex = set(stopwords.words('english'))

    success = False

    for i in range(5):
        try:

            response = requests.get(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
            success = True
            break
        except:
            print('failed attempt', i)

    if not success:
        return None

    text = response.text

    sentences = text.split('.')

    for sentence in sentences:

        sentence = sentence.lower().strip()
        sentence = re.sub('[^a-z]', ' ', sentence)

        words = sentence.split(' ')

        for word in words:
            if word == '' or word in stopLex:
                continue
            else:

                freq[word] = freq.get(word, 0) + 1

    word1 = freq.get(w1, 0)
    word2 = freq.get(w2, 0)

    sortedByValue = sorted(freq.items(), key=itemgetter(1), reverse=True)
    for i in range(len(sortedByValue)):
        if sortedByValue[i][1] > word1 and sortedByValue[i][1] < word2:
            result.add(sortedByValue[i][0])
    return result


if __name__ == '__main__':
    print(run('https://gist.githubusercontent.com/corydolphin/d2d76dae81df22a18d036244979c3c7b/raw/f3237ee708b4f685a5e5ded3514afcf0863768aa/Speech.txt', "mj", "work"))
