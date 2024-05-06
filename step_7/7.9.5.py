# Цифровой корень

n = int(input())
digital_sqr = 0
while n != 0:
    digital_sqr += n % 10
    if n // 10 == 0 and digital_sqr // 10 != 0:
        n = digital_sqr
        digital_sqr = 0
    else:
        n //= 10
print(digital_sqr)
