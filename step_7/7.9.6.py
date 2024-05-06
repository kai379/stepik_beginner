# Сумма факториалов

n = int(input())
fact = 1
sum_fact = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        fact *= j
    sum_fact += fact
    fact = 1
print(sum_fact)
