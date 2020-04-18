# Diploma Anna Simakova aka walkdis 2020
# set environment variables PYTHONHASHSEED=0
import os

import gensim
from keras import Sequential
from keras.layers import LSTM, Dense
import numpy as np
import re
#export PYTHONHASHSEED=0
#os.environ['PYTHONHASHSEED'] = '0'


# fix random seed for reproducibility
np.random.seed(1)
# my new method to change data
def string_to_int(input):
    output = "0"
    for i in input:
        if (re.search('[0-9]', i) is not None) and (output[len(output)-1] != "1"):
            output += "1"
        if (re.search('[a-z]', i) is not None) and (output[len(output)-1] != "2"):
            output += "2"
        if (re.search('[A-Z]', i) is not None) and (output[len(output)-1] != "3"):
            output += "3"
        if (re.search('[а-яё]', i) is not None) and (output[len(output)-1] != "4"):
            output += "4"
        if (re.search('[А-ЯЁ]', i) is not None) and (output[len(output)-1] != "5"):
            output += "5"
        if (re.search('[^a-zA-Z0-9а-яА-ЯЁё.,;:]', i) is not None) and (output[len(output)-1] != "6"):
            output += "6"
    return int(output)


# get ready data
sentenses = []
final_arr = np.array([], int)
final_word = []
answers = np.array([], int)
for i in range(20):
    for j in range(20):
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
            else:
                answers = np.append(answers, [0, 1])
            # answers = np.append(answers, int(unos))
k = 0
for sentense in sentenses:
    model1 = gensim.models.Word2Vec([sentense], min_count=1, window=10, size=5, sg=1)
    # size - changeble, find out best size
    for word in sentense:
        arr = [final_arr[k]]
        for e in model1[word].reshape(5):
            arr.append(e)
        final_word.append(arr)
        k = k+1

try_arr = np.asarray(final_word)

# final_arr - list of vectors, answer - list of answers, final_arr[0] -> answers[0] and so on
# possible add to final_arr my method to change word2vec as 1st in vector, find out the best way (with or without)

# word2vec
X = try_arr.reshape((len(final_word), 6, 1))
y = answers.reshape((int(len(answers)/2), 2))
model = Sequential()
model.add(LSTM(1, input_shape=(6, 1), activation='softplus', recurrent_activation='softsign'))
model.add(Dense(2, activation='sigmoid'))
# compile model
# model.compile(loss='mse', optimizer='adam')
# model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.compile(optimizer='rmsprop', loss='mse')
# fit model
model.fit(X, y, epochs=10, shuffle=True, verbose=0)
# model.fit(X, y, epochs=10, shuffle=True, verbose=0)
# model.save('lstm_model2.h5')
s = "Менеджер по логистике company КАРОЛИНА-ЯРОСЛАВА робертович ДЕМЕНТЬЕВ от Комаров-Филиппов КСЕНИЯ-КИРИЛЛ " \
    "Валентинович ЗАЯВЛЕНИЕ Прошу перевести меня с 28.12.1504 г на должность заведующий копировально-множительным " \
    "бюро с 16.03.1946 года в связи с наличием вакантного места и соответствием моей квалификации и опыта для ее " \
    "занятия. 28 09 1376 года /ДАНИЛОВ/ герман Рудольфович-Никодимович ШЕВЕЛЕВ" \

lst = s.split()
test = []
out = []
model_out = gensim.models.Word2Vec([lst], min_count=1, window=10, size=5, sg=1)
for word in lst:
    out = [string_to_int(word)]
    for e in model_out[word].reshape(5):
        out.append(e)
    test.append(out)
test_np = np.asarray(test)
# for i in lst:
#     test = np.append(test, string_to_int(i))
test_np = test_np.reshape((len(test), 6, 1))
print(str(model.predict(test_np)))
