# Сумма чисел 2

n = int(input())

sum_of_num = 0
for i in range(1, n + 1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
        sum_of_num += i
print(sum_of_num)
