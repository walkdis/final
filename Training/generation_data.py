from random import *
import random
import string

letters = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']


# for name, surname, second_name, adres, gender, company, position
def choose_case(input_str):
    case_to_input = {
        0: input_str,
        1: input_str.lower(),
        2: input_str.upper()
    }
    number = randrange(3)
    output = case_to_input[number]
    return output


def get_phone():
    phone_to_me = {
        0: '+' + str(randrange(9)) + '-' + '(' + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + ')' + '-'
           + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + '-' + str(randrange(9)) + str(randrange(9)) +
           '-' + str(randrange(9)) + str(randrange(9)),
        1: str(randrange(9)) + '-' + '(' + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + ')' + '-'
           + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + '-' + str(randrange(9)) + str(randrange(9)) +
           '-' + str(randrange(9)) + str(randrange(9)),
        2: '+' + str(randrange(9)) + '-' + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + '-'
           + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + '-' + str(randrange(9)) + str(randrange(9)) +
           '-' + str(randrange(9)) + str(randrange(9)),
        3: '+' + str(randrange(9)) + '(' + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + ')'
           + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + '-' + str(randrange(9)) + str(randrange(9)) +
           '-' + str(randrange(9)) + str(randrange(9)),
        4: str(randrange(9)) + '-' + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + '-'
           + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + '-' + str(randrange(9)) + str(randrange(9)) +
           '-' + str(randrange(9)) + str(randrange(9)),
        5: str(randrange(9)) + '(' + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + ')'
           + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + '-' + str(randrange(9)) + str(randrange(9)) +
           '-' + str(randrange(9)) + str(randrange(9)),
        6: '+' + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + str(randrange(9))
           + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) +
           str(randrange(9)) + str(randrange(9)),
        7: '+' + str(randrange(9)) + '(' + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + ')'
           + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) +
           str(randrange(9)) + str(randrange(9)),
        8: str(randrange(9)) + '(' + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + ')' +
           str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) +
           str(randrange(9)) + str(randrange(9)),
        9: str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) +
           str(randrange(9)) + str(randrange(9)) + '-' + str(randrange(9)) + str(randrange(9)) + str(randrange(9)) +
           str(randrange(9))
    }
    number = randrange(10)
    phone = phone_to_me[number]
    return phone


# for name, surname, second_name
def get_name(file_name):
    f = open('generate/' + file_name + '.txt', encoding='utf-8', mode='r')
    content = f.read()
    contents = content.split()
    number = randrange(2)
    name_to_me = {
        0: contents[randrange(len(contents))],
        1: contents[randrange(len(contents))] + '-' + contents[randrange(len(contents))]
    }
    name = name_to_me[number]
    name = choose_case(name)
    return name


def get_numbers():
    number = randrange(6)
    number_for_me = {
        0: str(randrange(10000000000)),
        1: str(randrange(10000000)) + '-' + str(randrange(1000)),
        2: str(randrange(1000)) + letters[randrange(len(letters))] + str(randrange(100)) +
           letters[randrange(len(letters))] + str(randrange(100)),
        3: str(randrange(10000000)) + '/' + str(randrange(1000)),
        4: str(randrange(10000000)) + '-' + letters[randrange(len(letters))] + str(randrange(100)) +
           letters[randrange(len(letters))] + str(randrange(100)),
        5: str(randrange(10000000)) + '/' + letters[randrange(len(letters))] + str(randrange(100)) +
           letters[randrange(len(letters))] + str(randrange(100))
    }
    numbers = number_for_me[number]
    return numbers


def get_date():
    days = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'десятое',
            'одиннадцатое',
            'двенадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье', 'тридцатое']
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
              'декабря']
    years = ['тысяча девятьсот пятьдесят восьмого', 'две тысячи восьмого', 'две тысячи десятого', 'тысяча восемьсот '
                                                                                                  'двенадцатого',
             'тысяча девятьсот девяносто шестого', 'две тысячи двадцать первого', 'тясяча девятьстот'
                                                                                  ' девяносто второго']
    endings = [' года', ' г.', ' г', ' год.', '']
    number = randrange(6)
    month = randrange(12) + 1
    day = randrange(31) + 1
    if month < 10:
        result = '0' + str(month)
    else:
        result = str(month)
    if day < 10:
        day_result = '0' + str(day)
    else:
        day_result = str(day)
    date_for_me = {
        0: day_result + '.' + result + '.' + str(randrange(2020)),
        1: day_result + '/' + result + '/' + str(randrange(2020)),
        2: day_result + ' ' + months[randrange(len(months))] + ' ' + str(randrange(2020)),
        3: days[randrange(len(days))] + ' ' + months[randrange(len(months))] + ' ' + years[randrange(len(years))],
        4: day_result + ' ' + result + ' ' + str(randrange(2020)),
        5: day_result + '/' + months[randrange(len(months))] + '/' + str(randrange(2020))
    }
    date = date_for_me[number] + endings[randrange(len(endings))]
    return date


def get_auto():
    num = randrange(1000)
    if num < 100:
        result = '0' + str(num)
    else:
        result = str(num)
    return letters[randrange(len(letters))] + result + letters[randrange(len(letters))] + \
           letters[randrange(len(letters))] + ' ' + str(randrange(1000))


def get_gender():
    gender = ['м', 'муж.', 'муж', 'мужской', 'ж', 'жен.', 'жен', 'женский']
    return gender[randrange(len(gender))]


def split_money(money):
    gitting = money
    if len(money) > 3:
        gitting = ''
        for i in range((len(money) // 3) + 1):
            if i == (len(money) // 3):
                gitting = money[:(len(money) - i * 3)] + gitting
            else:
                gitting = ' ' + money[(len(money) - (i + 1) * 3):(len(money) - i * 3)] + gitting
    if gitting[0] == ' ':
        gitting = gitting[1:]
    return gitting


def get_money():
    money = randrange(10000000000)
    endings = [' рублей', ' руб.', ' р.', '']
    answers = ['одна тысяча', 'две тысячи восемьсот сорок пять', 'пятьдесят миллионов четыреста пятьдесят шесть тысяч '
                                                                 'триста сорок пять', 'две тысячи сорок пять']
    moneys = {
        0: str(money) + endings[randrange(len(endings))],
        1: split_money(str(money)) + endings[randrange(len(endings))],
        2: answers[randrange(len(answers))] + endings[randrange(len(endings))],
        3: str(money) + endings[randrange(len(endings))] + ' (' + answers[randrange(len(answers))] +
           endings[randrange(len(endings))] + ')',
        4: split_money(str(money)) + endings[randrange(len(endings))] + ' (' + answers[randrange(len(answers))] +
           endings[randrange(len(endings))] + ')'
    }
    number = randrange(5)
    answer = moneys[number]
    return answer


def str_rand(str_len):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(str_len))


def get_mail():
    return str_rand(randrange(6) + 4) + '@' + str_rand(randrange(4) + 3) + '.' + str_rand(3)


def get_mult(file_name: string):
    f = open('generate/' + file_name + '.txt', encoding='utf-8', mode='r')
    content = f.read()
    contents = content.split('\n')
    return choose_case(contents[randrange(len(contents))])


def get_uno(text: string):
    splitty = text.split()
    unos = ''
    for i in range(len(splitty)):
        unos = unos + ' 1'
    return unos
# a = get_mult('adres')
# print(a)
