# Наибольшие числа

n = int(input())
num = 0
max_num_1 = 0
max_num_2 = 0
for _ in range(n):
    num = int(input())
    if num > max_num_1:
        max_num_1, max_num_2 = num, max_num_1
    elif num > max_num_2:
        max_num_2 = num
print(f'{max_num_1}\n{max_num_2}')
