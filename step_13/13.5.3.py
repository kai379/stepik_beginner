# Is a Number Prime? 🌶️

# объявление функции
def is_prime(num):
    flag = True
    if num == 1:
        flag = False
    else:
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
    return flag


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
