# Автомобильный номер
# АВЕКМНОРСТУХ

lp_number = input()
is_lp_number = True
for i in range(len(lp_number)):
    if i == 0 or i == 4 or i == 5:  # проверка букв
        if lp_number[i] not in 'АВЕКМНОРСТУХ':
            is_lp_number = False
    elif i == 1 or i == 2 or i == 3:  # проверка цифр внутри
        if not lp_number[i].isdigit():
            is_lp_number = False
    elif (i == 6 or i == 7 or i == 8 or i == 9) and (len(lp_number[7:]) == 2 or len(lp_number[7:]) == 3):  # проверка кода региона
        if lp_number[6] != '_':
            is_lp_number = False
        else:
            if len(lp_number) == 9 and i != 6:
                if not lp_number[i].isdigit():
                    is_lp_number = False
            elif len(lp_number) == 10 and i != 6:
                if not lp_number[i].isdigit():
                    is_lp_number = False
    else:
        is_lp_number = False

if is_lp_number:
    print('YES')
else:
    print('NO')

# 1) проверить по длине строки, потом
# 2) отделить буквы, цифры и знаки срезами -> делать их проверки отдельно
#
# s = input()
# flag = 'NO'
# correct_letters = 'АВЕКМНОРСТУХ'
#
# if 9 <= len(s) <= 10:
#     letters = s[0] + s[4:6]
#     digits = s[1:4] + s[7:]
#     underscore = s[6]
#
#     if digits.isdigit() and underscore == "_":
#         flag = 'YES'
#
#     for c in letters:
#         if c not in correct_letters:
#             flag = 'NO'
#
# print(flag)
