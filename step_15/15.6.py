# 1AF2 в 16

base_2 = ['0', '1']
base_9 = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
base_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
num = input('Число:  ')
base_num = int(input('База числа:  '))
# base_num_tr = int(input('База нового числа:  '))
num_10 = 0
num_ver = num[::-1]
for i in range(len(num_ver)):
    if base_num == 16:
        num_10 += base_16.index(num_ver[i]) * base_num ** i
    elif base_num == 2:
        num_10 += base_2.index(num_ver[i]) * base_num ** i

print(num_10)

