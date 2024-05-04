# Вторая цифра
# Дано натуральное число n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

n = int(input())
second_digit = 0
while n != 0:
    last_digit = n % 10
    if n // 100 == 0 and n // 10 != 0:
        second_digit = last_digit
    n //= 10
print(second_digit)
