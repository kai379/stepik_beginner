# Необычное сравнение

str01 = input().lower()
str02 = input().lower()
str01_alpha = ''
str02_alpha = ''

for ch in str01:
    if ch.isalpha():
        str01_alpha += ch

for ch in str02:
    if ch.isalpha():
        str02_alpha += ch

if str01_alpha == str02_alpha:
    print('YES')
else:
    print('NO')
