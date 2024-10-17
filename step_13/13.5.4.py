# Next Prime 🌶️🌶️

# объявление функции
def get_next_prime(num):
    flag = True
    num += 1
    while flag:
        for i in range(2, num):
            if num % i == 0:
                num += 1
                continue
        return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))


# stepik
#
# def is_prime(num):
#     if num == 1:
#         return False  # число 1 не является простым
#
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False  # сразу возвращает False, когда находим делитель
#
#     return True
#
#
# # объявление функции
# def get_next_prime(num):
#     cur_num = num + 1  # начинаем искать следующее простое число
#
#     while not is_prime(cur_num):  # если следующее число непростое, то увеличиваем на 1
#         cur_num += 1
#
#     return cur_num
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))
