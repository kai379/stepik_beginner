# Таблица-3 Таблица сложения

n = int(input())
for i in range(n):
    for j in range(9):
        print(f"{i + 1} + {j + 1} = {(i + 1) + (j + 1)}")
    print()
