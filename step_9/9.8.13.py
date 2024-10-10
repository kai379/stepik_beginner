# Название класса
# 0-9 вкл + А-П вкл

num = int(input())
class_num = None

for i in range(num):
    class_num = input()
    if len(class_num) == 2 and class_num[0].isdigit() and 'А' <= class_num[1] <= 'П':
        print('YES')
    else:
        print('NO')
