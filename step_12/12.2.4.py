# Валидный номер 🌶️🌶️
# abc-def-hijk или
# 7-abc-def-hijk,
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
# Телефонный номер должен содержать только цифры и символ -, а количество цифр в каждой группе должно быть правильным.
is_tel_numb = False
s = input()
if len(s) == 12 and s[3] == '-' and s[7] == '-':
    s = s.split('-')
    for i in s:
        if not i.isdigit():
            is_tel_numb = False
            break
        else:
            is_tel_numb = True
elif len(s) == 14 and s[0] == '7' and s[1] == '-' and s[5] == '-' and s[9] == '-':
    s = s.split('-')
    for i in s:
        if not i.isdigit():
            is_tel_numb = False
            break
        else:
            is_tel_numb = True

if is_tel_numb:
    print('YES')
else:
    print('NO')
