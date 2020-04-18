import numpy as np
import re
import gensim


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
for i in range(10):
    f = open('Training/test/' + str(i + 1) + '_' + '1.txt', encoding='utf-8', mode='r')
    a = open('Training/train/' + str(i + 1) + '_' + '1_answer.txt', encoding='utf-8', mode='r')
    go = f.read().split()
    ay = a.read().split()
    sentenses.append(go)
    answers.append()
    for word in go:
        final_arr = np.append(final_arr, string_to_int(word))
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