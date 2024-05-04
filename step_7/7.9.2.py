# Численный треугольник 3
# 1
# 121
# 12321
# 1234321
# 123454321

n = int(input())
for i in range(n):
    seredina = (i * 2 + 1) // 2 + 1
    for j in range(1, i * 2 + 2):
        print(seredina - abs(j - seredina), end='')
    print()
