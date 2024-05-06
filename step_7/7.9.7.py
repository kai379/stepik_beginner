# Простые числа

a = int(input())
b = int(input())
is_simple = True
for i in range(a, b + 1):
    for j in range(2, i):
        if i % j == 0:
            is_simple = False
    if is_simple and i != 1:
        print(i)
    else:
        is_simple = True

