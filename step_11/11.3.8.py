s = 'abcdefghijklmnopqrstuvwxyz'
list01 = []
for i in range(len(s)):
    list01.append(s[i] * (i + 1))

print(list01)

list02 = list(chr(ord('a') + i) * (i + 1) for i in range(len(s)))
print(list02)
