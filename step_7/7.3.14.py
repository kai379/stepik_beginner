# Only even numbers

QUANTITY_OF_NUMBERS = 10
flag = True
for _ in range(QUANTITY_OF_NUMBERS):
    num = int(input())
    if num % 2 != 0:
        flag = False
if flag:
    print('YES')
else:
    print('NO')
