from Training.generation_data import *
import re

for i in range(10):
    for j in range(1):
        f = open("generate/" + str(i+1) + '.txt', encoding='utf-8', mode='r')
        content = f.read()
        contents = content.split()
        final_text = ''
        answer_text = ''
        for b in range(len(contents)):
            if re.match(r'.*surname\d+.*', contents[b]):
                changing = get_name('surname')
                final_text = final_text + ' ' + re.sub(r'surname\d+', changing, contents[b])
                answer_text = answer_text + ' 1'
            elif re.match(r'.*name\d+.*', contents[b]) and not re.match(r'.*second_name\d+.*', contents[b]):
                changing = get_name('name')
                final_text = final_text + ' ' + re.sub(r'name\d+', changing, contents[b])
                answer_text = answer_text + ' 1'
            elif re.match(r'.*second_name\d+.*', contents[b]):
                changing = get_name('second')
                final_text = final_text + ' ' + re.sub(r'second_name\d+', changing, contents[b])
                answer_text = answer_text + ' 1'
            elif re.match(r'.*numbers\d+.*', contents[b]):
                changing = get_numbers()
                final_text = final_text + ' ' + re.sub(r'numbers\d+', changing, contents[b])
                answer_text = answer_text + ' 1'
            elif re.match(r'.*phone\d+.*', contents[b]):
                changing = get_phone()
                final_text = final_text + ' ' + re.sub(r'phone\d+', changing, contents[b])
                answer_text = answer_text + ' 1'
            elif re.match(r'.*mail\d+.*', contents[b]):
                changing = get_mail()
                final_text = final_text + ' ' + re.sub(r'mail\d+', changing, contents[b])
                answer_text = answer_text + ' 1'
            elif re.match(r'.*pas\d+.*', contents[b]):
                changing = get_name('pas')
                final_text = final_text + ' ' + changing
                answer_text = answer_text + ' 1'
            elif re.match(r'.*position\d+.*', contents[b]):
                changing = get_mult('position')
                final_text = final_text + ' ' + re.sub(r'position\d+', changing, contents[b])
                answer_text = answer_text + get_uno(changing)
            elif re.match(r'.*company\d+.*', contents[b]):
                changing = get_mult('company')
                final_text = final_text + ' ' + re.sub(r'company\d+', changing, contents[b])
                answer_text = answer_text + get_uno(changing)
            elif re.match(r'.*date\d+.*', contents[b]):
                changing = get_date()
                final_text = final_text + ' ' + re.sub(r'date\d+', changing, contents[b])
                answer_text = answer_text + get_uno(changing)
            elif re.match(r'.*adres\d+.*', contents[b]):
                changing = get_mult('adres')
                final_text = final_text + ' ' + re.sub(r'adres\d+', changing, contents[b])
                answer_text = answer_text + get_uno(changing)
            elif re.match(r'.*money\d+.*', contents[b]):
                changing = get_money()
                final_text = final_text + ' ' + re.sub(r'money\d+', changing, contents[b])
                answer_text = answer_text + get_uno(changing)
            elif re.match(r'.*gender\d+.*', contents[b]):
                changing = get_gender()
                final_text = final_text + ' ' + re.sub(r'gender\d+', changing, contents[b])
                answer_text = answer_text + ' 1'
            elif re.match(r'.*auto\d+.*', contents[b]):
                changing = get_auto()
                final_text = final_text + ' ' + re.sub(r'auto\d+', changing, contents[b])
                answer_text = answer_text + get_uno(changing)
            else:
                final_text = final_text + ' ' + contents[b]
                answer_text = answer_text + ' 0'
        while ' ' == final_text[0]:
            final_text = final_text[1:]
        while True:
            if answer_text[0] != ' ':
                break
            answer_text = answer_text[1:]
        p = open("test/" + str(i+1) + '_' + str(j+1) + '.txt', encoding='utf-8', mode='w+')
        a = open("test/" + str(i+1) + '_' + str(j+1) + '_answer.txt', encoding='utf-8', mode='w+')
        p.write(final_text)
        a.write(answer_text)
        # print(final_text, '\n', answer_text)


# # подстановка данных из списка (видимо, с пометкой принадлежности)
# text = 'adres'
# # генерация ответов
# word_to_answer = {
#     'surname': '1',
#     'name': '1',
#     'second_name': '1',
#     'numbers': '1',
#     'phone': '1',
#     'mail': '1',
#     'pas': '1',
#     'position': get_uno(get_mult('position')),
#     'company': get_uno(get_mult('company')),
#     'date': get_uno(get_date()),
#     'adres': get_uno(get_mult('adres')),
#     'money': get_uno(get_money()),
#     'gender': '1',
#     'auto': get_uno(get_auto())
# }
# mult = ''
# if text in word_to_answer:
#     mult = word_to_answer[text]
# else:
#     mult = '0'
#
# print(mult)
