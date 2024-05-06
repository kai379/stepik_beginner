text = input().lower()
count_vowel = 0
count_consonant = 0
for i in range(len(text)):
    if text[i] in 'ауоыиэяюе':
        count_vowel += 1
    if text[i] in 'бвгджзйклмнпрстфхцчшщ':
        count_consonant += 1
print(f'Количество гласных букв равно {count_vowel}')
print(f'Количество согласных букв равно {count_consonant}')
