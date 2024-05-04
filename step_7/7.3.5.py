# Напишите программу, которая подсчитывает количество чисел в диапазоне от
# a до b (включительно), куб которых оканчивается на 4 или 9.

a, b = int(input()), int(input())
DEGREE = 3
LUST_NUM_1 = 4
LUST_NUM_2 = 9
count = 0
for i in range(a, b + 1):
    if (i ** DEGREE) % 10 == LUST_NUM_1 or (i ** DEGREE) % 10 == LUST_NUM_2:
        count += 1
print(count)
