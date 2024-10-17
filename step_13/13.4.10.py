# найти всех

# объявление функции
def find_all(target, symbol):
    target_list = list(target)
    symbol_index = []
    for i in range(len(target_list)):
        if target_list[i] == symbol:
            symbol_index.append(i)
    return symbol_index


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
