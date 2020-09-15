#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Установить PyInstaller
# pip uninstall pyinstaller
# pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip

# Создать приложение в один файл командой: (перед этим удалить папки dist и build в корне проект)
# pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" single_flaskapp.py

# Хз как пофиксить изначальное открытие в Internet Explorer, потому что потом оно закроет его и открое дефолтный браузер
# Так же известная проблема, что если мы закроем вкладку в браузере, приложение продолжит висеть в памяти и его надо закрыть через Task Manager

import sys
import os
import webbrowser
from threading import Timer
from flask import Flask, render_template, request
from flask import json
import gensim
import numpy as np
import re


# my new method to change data
from tensorflow_core.python.keras.models import load_model


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

# Конфигурация для того, чтобы приложение было независимым
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)


# Открываем браузер по-умолчанию при запуске приложения
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')


# Основной маршрут, открывает приложение
@app.route('/')
def index():
    return render_template('app.html', name='test')


# Хэндлим POST запрос с данными для обработки
@app.route('/run', methods=['POST'])
def run():
    # Получаем отправленные данные
    type_to_work = request.form['type']  # Типы - default, simple, highlight
    text_to_work = request.form['text']  # Сам текст
    sentenses = []
    test_arr = np.array([], int)
    test_word = []
    go = text_to_work.split()
    sentenses.append(go)
    for word in go:
        test_arr = np.append(test_arr, string_to_int(word))
    k = 0
    for sentense in sentenses:
        model1 = gensim.models.Word2Vec([sentense], min_count=1, window=10, size=5, sg=1)
        # size - changeble, find out best size
        for word in sentense:
            arr = [test_arr[k]]
            for e in model1[word].reshape(5):
                arr.append(e)
            test_word.append(arr)
            k = k + 1
    test_np = np.asarray(test_word)
    test_np = test_np.reshape((len(test_word), 6, 1))
    model = load_model("test.h5")
    # compile model
    model.compile(loss='binary_crossentropy', optimizer='adam')
    # predict
    answer = model.predict_proba(test_np)
    text_ready = ''
    for p in range(len(answer)):
        if answer[p][0] >= answer[p][1]:
            go[p] = '***'
        text_ready = text_ready + go[p] + ' '

    # TODO Здесь запускаем функцию которая обработает текст из text_to_work
    # Если надо обернуть часть текста в ЖЕЛТЫЙ МАРКЕР, то его необходимо поместить в тег <span class="marker marker_yellow">text</span>
    # text_ready = text_to_work  # Готовый текст
    # Создаем ответ и передаем готовый текст в поле 'data'
    response = app.response_class(
        response=json.dumps({'status': 'ok', 'data': text_ready}),
        status=200,
        mimetype='application/json'
    )
    return response


# Запускаем приложение
if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run()
