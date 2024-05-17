# Суммы двух

n = int(input())
list_num = []
list_res = []

for _ in range(n):
    list_num.append(int(input()))

for i in range(len(list_num) - 1):
    list_res.append(list_num[i] + list_num[i + 1])

print(list_res)


# n, a = int(input()), int(input())
# lst = []
# for _ in range(n-1):
#     b = int(input())
#     lst.append(a + b)
#     a = b
# print(lst)
