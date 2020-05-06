import numpy as numpy
import os
from keras import preprocessing
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, Bidirectional
from keras import optimizers

# Variables for paths
path_train = './datasets/'
# path_test = './test-data.txt'  # change file name

# Load Training Data
x = []
y = []
for i, j, k in os.walk(path_train):
    for file in k:
        if (file.endswith('.txt')):
            paths = path_train + file
            f = open(paths)
            for line in f:
                if (len(line.strip().split('\t')) == 2):
                    review, target = line.strip().split('\t')
                    x.append(review.lower())
                    y.append(int(target[0]))
            f.close()

# print("The size of training dataset is " + str(len(x)))

# Text processing for training reviews
vocabulary = 10000
word_num = 15
tokenizer = preprocessing.text.Tokenizer(num_words=vocabulary)
tokenizer.fit_on_texts(x)
word_index = tokenizer.word_index
embedded_sentences = tokenizer.texts_to_sequences(x)
X = preprocessing.sequence.pad_sequences(
    embedded_sentences, maxlen=word_num)

# # Load Test Data for submission
# x_test = []
# f = open(path_test)
# for line in f:
#     x_test.append(line.strip().lower())
# f.close()

# print("The size of testing dataset is " + str(len(x_test)))

indices = int(len(x) * 0.9)
X_train = X[:indices]
Y_train = y[:indices]
X_test = X[indices:]
Y_test = y[indices:]

print("The size of training dataset is " + str(len(X_train)))
print("The size of test dataset is " + str(len(X_test)))

###### RNN ######
embedding_dim = 32
state_dim = 32

model = Sequential()
model.add(Embedding(vocabulary, embedding_dim, input_length=word_num))
model.add(Bidirectional(LSTM(state_dim, return_sequences=False, dropout=0.2)))
model.add(Dense(1, activation='sigmoid'))

model.summary()

epochs = 3
model.compile(optimizer=optimizers.RMSprop(lr=0.001),
              loss='binary_crossentropy', metrics=['acc'])
history = model.fit(X_train, Y_train, epochs=epochs, batch_size=32, verbose=1)

# Text processing for training reviews
# vocabulary = 10000
# word_num = 15
# tokenizer = preprocessing.text.Tokenizer(num_words=vocabulary)
# tokenizer.fit_on_texts(x_test)
# word_index = tokenizer.word_index
# embedded_sentences = tokenizer.texts_to_sequences(x_test)
# X_test = preprocessing.sequence.pad_sequences(
#     embedded_sentences, maxlen=word_num)

loss_and_acc = model.evaluate(X_test, Y_test, verbose=0)
print('loss = ' + str(loss_and_acc[0]))
print('acc = ' + str(loss_and_acc[1]))

# # Prediction Output for Submission
# pred = model.predict_classes(X_test)
# pred = pred.reshape(-1)
# output_array = []
# for x in pred:
#     output_array.append(x)

# fout = open("pred_result.txt", "w")
# for x in output_array:
#     fout.write(str(x) + "\n")
# fout.close()
