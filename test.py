import re


# my old method to change data
def string_to_int(input):
    output = ""
    for i in input:
        if (re.search('[0-9]', i) is not None) and not ("1" in output):
            output += "1"
        if (re.search('[a-z]', i) is not None) and not ("2" in output):
            output += "2"
        if (re.search('[A-Z]', i) is not None) and not ("3" in output):
            output += "3"
        if (re.search('[а-яё]', i) is not None) and not ("4" in output):
            output += "4"
        if (re.search('[А-ЯЁ]', i) is not None) and not ("5" in output):
            output += "5"
        if (re.search('[^a-zA-Z0-9а-яА-ЯЁё.,;:]', i) is not None) and not ("6" in output):
            output += "6"
    return int(output)



# my new method to change data
def string_to_int1(input):
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


s = "He1%$11L1lO"
answ = string_to_int1(s)
print(answ)
