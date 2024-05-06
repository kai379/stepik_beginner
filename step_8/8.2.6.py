# Все вместе 2
# Дано натуральное число. Напишите программу, которая вычисляет:
#
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречаются цифры 0 и 5 (всего суммарно).

n = int(input())
count_of_3 = 0
last_digit_count = 0
last_digit_num = n % 10
honest_count = 0
more_5_sum = 0
product_more_7 = 1
zero_or_five_count = 0

while n != 0:
    last_digit = n % 10
    if last_digit == 3:
        count_of_3 += 1
    if last_digit == last_digit_num:
        last_digit_count += 1
    if last_digit % 2 == 0:
        honest_count += 1
    if last_digit > 5:
        more_5_sum += last_digit
    if last_digit > 7:
        product_more_7 *= last_digit
    if last_digit == 0 or last_digit == 5:
        zero_or_five_count += 1
    n //= 10
print(f"{count_of_3}\n{last_digit_count}\n{honest_count}\n{more_5_sum}\n{product_more_7}\n{zero_or_five_count}")
