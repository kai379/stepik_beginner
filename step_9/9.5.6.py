# никнейм должен начинаться с символа @
# никнейм должен содержать от 5 до 15 (включительно) символов (включая первый символ @)
# никнейм должен содержать только строчные буквы и цифры (помимо первого символа @)

s = input()
if s.startswith('@') and 5 <= len(s) <= 15 and \
        ((s[1:].isalnum() and s.islower()) or (s[1:].isalpha() and s.islower()) or s[1:].isdigit()):
    print('Correct')
else:
    print('Incorrect')
