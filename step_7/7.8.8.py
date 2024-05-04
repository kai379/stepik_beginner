# Звездный треугольник
# Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный
# звездный треугольник с основанием, равным n в соответствии с примером:

n = int(input())
for i in range(n // 2 + 1):
    for j in range(i + 1):
        print('*', end='')
    print()
for i in range(n // 2):
    for j in range(n // 2 - i):
        print('*', end='')
    print()


# n = int(input())
# for i in range(n):
#     cur_cnt = (n // 2 + 1) - abs(n // 2 - i)
#     for j in range(cur_cnt):
#         print("*", end="")
#     print()
