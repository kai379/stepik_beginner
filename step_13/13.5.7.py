# Палиндром 🌶️

# объявление функции
def is_palindrome(text):
    text_lower = text.lower()
    text_clear = [c for c in text_lower if c.isalpha()]
    text_reverse = text_clear.copy()
    text_reverse.reverse()
    return text_clear == text_reverse


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))


######
# # объявление функции
# def is_palindrome(text):
#     text = [i.lower() for i in text if i not in (',.!?- ')]
#     return text == text[::-1]
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_palindrome(txt))


# ###
# def is_palindrome(text):
#     p = []
#     for c in text:
#         if c.isalpha(): p.append(c.lower())
#     return p == p[::-1]
#
# print(is_palindrome(input()))
