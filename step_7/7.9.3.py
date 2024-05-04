# Делители-1

a = int(input())
b = int(input())
sum_of_div = 0
sum_of_div_max = 0
num = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            sum_of_div += j
    if sum_of_div >= sum_of_div_max:
        num = i
        sum_of_div_max = sum_of_div
    sum_of_div = 0
print(num, sum_of_div_max)
