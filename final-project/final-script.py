import numpy as numpy
import os
from keras import preprocessing
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, Bidirectional
from keras import optimizers

# Variables for paths
path_test = './test-data.txt'  # ******change test dataset file name******

# Load Training Data
x_train = []
y_train = []

f = open("training-datasets.txt")
for line in f:
    if (len(line.strip().split('\t')) == 2):
        review, target = line.strip().split('\t')
        x_train.append(review.lower())
        y_train.append(int(target[0]))
f.close()

print("The size of training dataset is " + str(len(x_train)))

# Text processing for training reviews
vocabulary = 10000
word_num = 15
tokenizer = preprocessing.text.Tokenizer(num_words=vocabulary)
tokenizer.fit_on_texts(x_train)
word_index = tokenizer.word_index
embedded_sentences = tokenizer.texts_to_sequences(x_train)
X_train = preprocessing.sequence.pad_sequences(
    embedded_sentences, maxlen=word_num)

Y_train = y_train

# Load Test Data for submission
x_test = []
f = open(path_test)
for line in f:
    x_test.append(line.strip().lower())
f.close()

print("The size of testing dataset is " + str(len(x_test)))

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
vocabulary = 10000
word_num = 15
tokenizer = preprocessing.text.Tokenizer(num_words=vocabulary)
tokenizer.fit_on_texts(x_test)
word_index = tokenizer.word_index
embedded_sentences = tokenizer.texts_to_sequences(x_test)
X_test = preprocessing.sequence.pad_sequences(
    embedded_sentences, maxlen=word_num)

# Prediction Output for Submission
pred = model.predict_classes(X_test)
pred = pred.reshape(-1)
output_array = []
for x in pred:
    output_array.append(x)

fout = open("pred_result.txt", "w")
for x in output_array:
    fout.write(str(x) + "\n")
fout.close()
