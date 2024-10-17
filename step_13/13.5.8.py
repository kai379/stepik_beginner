# BEEGEEK 🐝


# объявление функции
def is_valid_password(password):
    password_split = password.split(':')
    if is_valid(password_split):
        if is_palindrome(password_split[0]) and is_prime(password_split[1]) and is_even(password_split[2]):
            return True
        else:
            return False
    else:
        return False


def is_prime(b):
    b_num = int(b)
    if b_num == 1:
        return False
    else:
        for i in range(2, b_num):
            if b_num % i == 0:
                return False
        return True


def is_palindrome(a):
    if a == a[::-1]:
        return True
    else:
        return False


def is_even(c):
    c_num = int(c)
    if c_num % 2 == 0:
        return True
    else:
        return False


def is_valid(psw_split):
    if len(psw_split) == 3 and psw_split[0].isdigit() and psw_split[1].isdigit() and psw_split[2].isdigit():
        return True
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))

