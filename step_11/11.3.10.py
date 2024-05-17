# Список делителей

n = int(input())
list01 = []
for i in range(1, n + 1):
    if n % i == 0:
        list01.append(i)

print(list01)
