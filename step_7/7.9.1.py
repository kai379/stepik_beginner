# Численный треугольник 2
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
n = int(input())
count = 1
for i in range(n):
    for _ in range(i + 1):
        print(count, end=' ')
        count += 1
    print()
