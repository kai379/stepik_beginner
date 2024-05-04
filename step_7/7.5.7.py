# Все вместе
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

n = int(input())
sum_of_num = 0
len_of_num = 0
product_of_num = 1
average_of_num = 0
first_num = 0
sum_of_first_and_last = 0

while n != 0:
    last_digit = n % 10
    if len_of_num == 0:
        sum_of_first_and_last += last_digit
    sum_of_num += last_digit
    product_of_num *= last_digit
    len_of_num += 1
    n //= 10
    if n == 0:
        first_num = last_digit
        sum_of_first_and_last += last_digit
        average_of_num = sum_of_num / len_of_num
print(f'{sum_of_num}\n{len_of_num}\n{product_of_num}\n{average_of_num}\n{first_num}\n{sum_of_first_and_last}')
