# Асимптотическое приближение

from math import log

n = int(input())

result = 0
for i in range(1, n + 1):
    result += 1 / i

result -= log(n)
print(result)
