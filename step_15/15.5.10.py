eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input()
text_list = text.split()
word = ''
step = 0
# проход по списку с заменой на шифр
for i in range(len(text_list)):
    # длина слова без знаков
    for c in text_list[i]:
        if c.isalpha():
            step += 1
    # шифрование
    for c in text_list[i]:
        if not c.isalpha():
            word += c
        elif c in eng_upper_alphabet:
            word += eng_upper_alphabet[(eng_upper_alphabet.index(c) + step) % len(eng_upper_alphabet)]
        elif c in eng_lower_alphabet:
            word += eng_lower_alphabet[(eng_lower_alphabet.index(c) + step) % len(eng_lower_alphabet)]
    # замена слова в списке
    text_list[i] = word
    word = ''
    step = 0

print(*text_list)
