# Diploma Anna Simakova aka walkdis 2020
# set environment variables PYTHONHASHSEED=0
import os

import gensim
import tensorflow
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.python.keras.layers.cudnn_recurrent import CuDNNLSTM

from keras import regularizers
import numpy as np
import re

# export PYTHONHASHSEED=0
# os.environ['PYTHONHASHSEED'] = '0'


# fix random seed for reproducibility
np.random.seed(1)
tensorflow.config.list_physical_devices('GPU')


def hash(astring):
    q = 0
    for each in range(len(astring)):
        q = q + ord(astring[each])
    return q


# my new method to change data
def string_to_int(input):
    output = "0"
    for i in input:
        if (re.search('[0-9]', i) is not None) and (output[len(output) - 1] != "1"):
            output += "1"
        if (re.search('[a-z]', i) is not None) and (output[len(output) - 1] != "2"):
            output += "2"
        if (re.search('[A-Z]', i) is not None) and (output[len(output) - 1] != "3"):
            output += "3"
        if (re.search('[а-яё]', i) is not None) and (output[len(output) - 1] != "4"):
            output += "4"
        if (re.search('[А-ЯЁ]', i) is not None) and (output[len(output) - 1] != "5"):
            output += "5"
        if (re.search('[^a-zA-Z0-9а-яА-ЯЁё.,;:]', i) is not None) and (output[len(output) - 1] != "6"):
            output += "6"
    if len(output) > 10:
        output = output[:10]
    return int(output)


# get ready train data
sentenses = []
final_arr = np.array([], int)
final_word = []
answers = np.array([], int)
un = 0
zer = 0
for i in range(21):
    for j in range(10):
        f = open('Training/data/' + str(i + 1) + '_' + str(j + 1) + '.txt', encoding='utf-8', mode='r')
        a = open('Training/answers/' + str(i + 1) + '_' + str(j + 1) + '_answer.txt', encoding='utf-8', mode='r')
        go = f.read().split()
        ay = a.read().split()
        sentenses.append(go)
        for word in go:
            final_arr = np.append(final_arr, string_to_int(word))
        for unos in ay:
            if unos == '1':
                answers = np.append(answers, [1, 0])
                un += 1
            else:
                answers = np.append(answers, [0, 1])
                zer += 1
            # answers = np.append(answers, int(unos))
k = 0
for sentense in sentenses:
    model1 = gensim.models.Word2Vec([sentense], min_count=1, window=10, size=31, sg=1, workers=1, seed=1, hashfxn=hash)
    # size - changeble, find out best size
    for word in sentense:
        arr = [final_arr[k]]
        for e in model1[word].reshape(31):
            arr.append(e)
        final_word.append(arr)
        k = k + 1

try_arr = np.asarray(final_word)

# get ready test data
sentenses = []
test_arr = np.array([], int)
test_word = []
answers1 = []
for i in range(21):
    for j in range(1):
        f = open('Training/test/' + str(i + 1) + '_' + str(j + 1) + '.txt', encoding='utf-8', mode='r')
        a = open('Training/test/' + str(i + 1) + '_' + str(j + 1) + '_answer.txt', encoding='utf-8', mode='r')
        go = f.read().split()
        ay = a.read().split()
        sentenses.append(go)
        for word in go:
            test_arr = np.append(test_arr, string_to_int(word))
        for unos in ay:
            answers1.append(int(unos))
k = 0
for sentense in sentenses:
    model1 = gensim.models.Word2Vec([sentense], min_count=1, window=10, size=31, sg=1, workers=1, seed=1, hashfxn=hash)
    # size - changeble, find out best size
    for word in sentense:
        arr = [test_arr[k]]
        for e in model1[word].reshape(31):
            arr.append(e)
        test_word.append(arr)
        k = k + 1

test_np = np.asarray(test_word)
test_np = test_np.reshape((len(test_word), 32, 1))



# final_arr - list of vectors, answer - list of answers, final_arr[0] -> answers[0]  and so on
# possible add to final_arr my method to change word2vec as 1st in vector, find out the best way (with or without)
print(str(un), str(zer))

# word2vec
X = try_arr.reshape((len(final_word), 32, 1))
y = answers.reshape((int(len(answers)/2), 2))
model = Sequential()
model.add(CuDNNLSTM(32, return_sequences=True))
model.add(CuDNNLSTM(13, return_sequences=True))
model.add(CuDNNLSTM(5))
model.add(Dense(2, activation='sigmoid'))
# compile model
# model.compile(loss='mse', optimizer='adam')
# model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.compile(optimizer='adam', loss='binary_crossentropy')
# fit model
model.fit(X, y, epochs=3950, verbose=2)
# model.fit(X, y, epochs=10, shuffle=True, verbose=0)
model.save('test_32_2_km_add_hash_new_data_adam_3950.h5')
answ = model.predict(test_np)
answer1 = []
for p in range(len(answ)):
    if answ[p][0] >= answ[p][1]:
        answer1.append(1)
    else:
        answer1.append(0)
print(answer1, '\n', answers1)
tensorflow.keras.backend.clear_session()
