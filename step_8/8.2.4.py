# Звездная рамка

n = int(input())
LINE_LENGTH = 19
START_LINE = 0
for i in range(n):
    if i == START_LINE or i == n - 1:
        print('*' * LINE_LENGTH)
    else:
        print("*" + " " * (LINE_LENGTH - 2) + "*")

