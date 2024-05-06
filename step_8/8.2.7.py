# # Числа Рамануджана
# число, выражаемое как сумма двух кубов двумя разными способами
# 1729 = 1^3+12^3=9^3+10^3

count = 0
DEGREE = 3
ram_1 = 0
ram_2 = 0
ram_3 = 0
ram_4 = 0
ram_5 = 0
flag = True
while flag:
    for a in range(1, 100):
        if not flag:
            break
        else:
            for b in range(1, 100):
                if not flag:
                    break
                else:
                    for c in range(1, 100):
                        if not flag:
                            break
                        else:
                            for d in range(1, 100):
                                if a != b and a != c and a != d and b != c and b != d and c != d:
                                    if a ** DEGREE + b ** DEGREE == c ** DEGREE + d ** DEGREE:
                                        ram_value = a ** DEGREE + b ** DEGREE
                                        if ram_1 == 0:
                                            ram_1 = ram_value
                                            print(ram_1)
                                        elif ram_2 == 0 and ram_value != ram_1:
                                            ram_2 = ram_value
                                            print(ram_2)
                                        elif ram_3 == 0 and ram_value != ram_1 and ram_value != ram_2:
                                            ram_3 = ram_value
                                            print(ram_3)
                                        elif ram_4 == 0 and ram_value != ram_1 and ram_value != ram_2 and ram_value != ram_3:
                                            ram_4 = ram_value
                                            print(ram_4)
                                        elif ram_5 == 0 and ram_value != ram_1 and ram_value != ram_2 and ram_value != ram_3 and ram_value != ram_4:
                                            ram_5 = ram_value
                                            print(ram_5)
                                            flag = False
                                            break





