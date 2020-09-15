import numpy as np
import re
import gensim
from tensorflow_core.python.keras.models import load_model


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
model = load_model("test_32_1_km_add_hash_new_data.h5")
answ = model.predict(test_np)
answer1 = []
for p in range(len(answ)):
    if answ[p] >= 0.5:
        answer1.append(1)
    else:
        answer1.append(0)
print(answer1, '\n', answers1)
