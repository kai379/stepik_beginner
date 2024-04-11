# Напишите программу, в которой рассчитывается сумма и
# произведение цифр положительного трехзначного числа.
#    Формат входных данных
# На вход программе подаётся положительное трёхзначное число.
#    Формат выходных данных
# Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.
# Sample Input 1:
# 123
# Sample Output 1:
# Сумма цифр = 6
# Произведение цифр = 6

number_to_calc = int(input())
sum_of_numb = number_to_calc % 10 + number_to_calc // 10 % 10 + number_to_calc // 100
mult_of_numb = (number_to_calc % 10) * (number_to_calc // 10 % 10) * (number_to_calc // 100)
print(f"Сумма цифр = {sum_of_numb}")
print(f"Произведение цифр = {mult_of_numb}")