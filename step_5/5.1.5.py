# YES or NO вот в чем вопрос
# Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».
# Условия:
# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».

n = int(input())
if n % 2 != 0:
    print('YES')
elif 2 <= n <= 5:
    if n % 2 == 0:
        print('NO')
    else:
        print('YES')
elif 6 <= n <= 20:
    if n % 2 == 0:
        print('YES')
    else:
        print('NO')
elif n > 20 and n % 2 == 0:
    print('NO')