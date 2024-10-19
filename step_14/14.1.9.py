# объявление функции
def is_magic(date):
    date_list = date.split('.')
    if int(date_list[0]) * int(date_list[1]) == int(date_list[2][2:]):
        return True
    return False


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
