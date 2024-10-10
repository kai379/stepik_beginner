# Строковые минимум и максимум

min_str = 'я'
max_str = 'А'
str_inp = input()

while str_inp != 'КОНЕЦ':
    if str_inp > max_str:
        max_str = str_inp
    if str_inp < min_str:
        min_str = str_inp
    str_inp = input()

print(f'Минимальная строка ⬇️: {min_str}'
      f'Максимальная строка ⬆️: {max_str}')

# s = input()
# mx_s = s
# mn_s = s
#
# while s != 'КОНЕЦ':
#     mn_s = min(mn_s, s)
#     mx_s = max(mx_s, s)
#
#     s = input()
#
# print(f'Минимальная строка ⬇️: {mn_s}')
# print(f'Максимальная строка ⬆️: {mx_s}')
