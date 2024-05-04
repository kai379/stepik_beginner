# Старинная задача
# Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги,
# если плата за быка – 10 рублей,
# за корову – 5 рублей,
# # за теленка – 0.5 рубля
# # и надо купить 100 голов скота?
# # Примечание. Используйте вложенный цикл for.

MONEY = 100
WOULD = 10
COW = 5
CALF = 0.5
QUANTITY = 100
for i in range(MONEY // WOULD):
    for j in range(MONEY // COW):
        for k in range(int(MONEY // CALF)):
            if MONEY - WOULD * i - COW * j - CALF * k == 0 and i + j + k == 100:
                print(f"Быков - {i}, Коров - {j}, Телят - {k}")
