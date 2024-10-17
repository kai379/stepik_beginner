# Правильная скобочная последовательность 🌶️
# объявление функции
def is_correct_bracket(text):
    list_txt = list(text)
    if is_valid(list_txt):
        while list_txt.count('(') != 0 or list_txt.count(')') != 0:
            if list_txt.index('(') < list_txt.index(')'):
                list_txt.remove('(')
                list_txt.remove(')')
            else:
                break
        if list_txt:
            return False
        else:
            return True
    return False


def is_valid(list_txt):
    if list_txt[0] == '(' and list_txt.count('(') == list_txt.count(')') and list_txt[-1] == ')':
        return True
    return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))


###
# # объявление функции
# def is_correct_bracket(text):
#     while "()" in text:
#         text = text.replace("()", "")
#
#     return text == ""
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))


###
# # объявление функции
# def is_correct_bracket(text):
#     cnt = 0
#     for el in text:
#         if el == "(":
#             cnt += 1
#         else:
#             cnt -= 1
#
#         if cnt == -1:
#             break
#
#     return cnt == 0
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))
