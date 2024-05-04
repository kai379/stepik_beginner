# Сумма делителей

n = int(input())
sum_of_divider = 0
for i in range(n + 1):
    if n % i == 0:
        sum_of_divider += i
print(sum_of_divider)
