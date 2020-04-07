from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import os


def getlabel(x):
    if x == 'comp.windows.x' or x == 'comp_os.ms-windows.misc' or x == 'comp.sys.ibm.pc.hardware' or x == 'comp.sys.mac.hardware' or x == 'comp.graphics' or x == 'misc.forsale' or x == 'sci.crypt':
        return 'comp'
    elif x == 'rec.sport.baseball' or x == 'rec.sports.hockey':
        return 'sport'
    elif x == 'talk.politics.misc' or x == 'talk.politics.mideast' or x == 'talk.politics.guns' or x == 'talk.religion.misc' or x == 'soc.religion.christian':
        return 'politics'
    elif x == 'rec.autos' or x == 'rec.motorcycles':
        return 'rec'


def loaddata(parent_dir):
    train_news = []
    test_news = []
    train_label = []
    test_label = []
    entries = os.listdir(parent_dir)
    entries.remove('.DS_Store')

    for child_dir in entries:
        path = os.path.join(parent_dir, child_dir)
        child_dirs = os.listdir(path)

        for file in child_dirs:
            files = os.path.join(path, file)
            news = []
            first_emptyLine = False
            f = open(files, encoding="ISO-8859-1")

            for line in f:
                if not first_emptyLine:
                    if line == '\n':
                        first_emptyLine = True
                        continue
                    else:
                        continue
                else:
                    news = line.strip().lower()

            if child_dir == 'comp.windows.x' or child_dir == 'rec.sport.baseball' or child_dir == 'talk.politics.misc' or child_dir == 'rec.autos':
                test_news.append(''.join(news))
                test_label.append(getlabel(child_dir))
            elif child_dir == 'comp_os.ms-windows.misc' or child_dir == 'sci.crypt' or child_dir == 'talk.religion.misc' or child_dir == 'misc.forsale' or child_dir == 'soc.religion.christian' or child_dir == 'comp.sys.ibm.pc.hardware' or child_dir == 'comp.sys.mac.hardware' or child_dir == 'comp.graphics' or child_dir == 'rec.sports.hockey' or child_dir == 'talk.politics.mideast' or child_dir == 'talk.politics.guns' or child_dir == 'rec.motorcycles':
                train_news.append(''.join(news))
                train_label.append(getlabel(child_dir))
            else:
                continue
        f.close()
    return test_news, test_label, train_news, train_label


test_news, test_label, train_news, train_label = loaddata('./20_newsgroups')

counter = CountVectorizer()
counter.fit(train_news)

counts_train = counter.transform(train_news)
counts_test = counter.transform(test_news)

clf = MultinomialNB()

clf.fit(counts_train, train_label)

pred = clf.predict(counts_test)

print(accuracy_score(pred, test_label))
