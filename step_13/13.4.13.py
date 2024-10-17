# Merge lists 2

# объявление функции
def merge(n_str):
    list_merge = list()
    for _ in range(n_str):
        list_merge += [int(i) for i in input().split()]
    list_merge.sort()
    return list_merge


# считываем данные
n = int(input())

# вызываем функцию
print(*merge(n))
