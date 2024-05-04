# Одинаковые цифры
# Дано натуральное число. Напишите программу, которая определяет,
# состоит ли указанное число из одинаковых цифр.

n = int(input())
flag = True
last_num = n % 10
while n != 0:
    last_digit = n % 10
    if last_num != last_digit:
        flag = False
    n //= 10

if flag:
    print('YES')
else:
    print('NO')
