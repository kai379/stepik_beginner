# Максимальная цифра
# Минимальная цифра

n = int(input())
max_num = -1
min_num = 10
while n != 0:
    last_digit = n % 10
    if last_digit > max_num:
        max_num = last_digit
    if last_digit < min_num:
        min_num = last_digit
    n //= 10
print(f'Максимальная цифра равна {max_num}\n'
      f'Минимальная цифра равна {min_num}')
