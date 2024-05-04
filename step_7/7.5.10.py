# Упорядоченные цифры
# Дано натуральное число. Напишите программу, которая определяет,
# является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

n = int(input())
flag = True
previous_digit = n % 10
while n != 0:
    last_digit = n % 10
    if last_digit < previous_digit:
        flag = False
    previous_digit = last_digit
    n //= 10
if flag:
    print('YES')
else:
    print('NO')
