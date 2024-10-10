# Какая следующая буква?

letter = input()
if ord(letter) == ord('Я'):
    print('Дальше букв нет')
else:
    print(chr(ord(letter) + 1))
