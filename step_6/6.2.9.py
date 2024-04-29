a, b, c = input(), input(), input()

MAX_LEN = max(len(a), len(b), len(c))
MIN_LEN = min(len(a), len(b), len(c))
SUM_LEN = len(a) + len(b) + len(c)
if MAX_LEN == SUM_LEN - MIN_LEN - MAX_LEN + (SUM_LEN - MIN_LEN - MAX_LEN) - MIN_LEN:
    print('YES')
else:
    print('NO')

# (2b-c-a)(2c-b-a)(2a-b-c) = 0

# if (2 * len_1 - len_2 - len_3) * (2 * len_2 - len_1 - len_3) * (2 * len_3 - len_1 - len_2) == 0:
#     print('YES')
# else:
#     print('NO')
