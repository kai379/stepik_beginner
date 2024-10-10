# Волшебное число

word = input()
word_sm = word
word_larg = word

for letter in range(3):
    word = input()
    word_sm = min(word, word_sm)
    word_larg = max(word, word_larg)

print((ord(word_sm[-1]) * ord(word_larg[-1])) ** 2)
