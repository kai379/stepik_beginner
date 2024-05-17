# k-ая буква слова

n = int(input())
list01 = []

for _ in range(n):
    list01.append(input())

k = int(input())

for i in list01:
    if len(i) >= k:
        print(i[k], end='')

