s = input()
flag = True
for i in range(len(s)//2):
    print(s[i], s[(- 1 * i) - 1])
    if s[i] != s[(i * -1) - 1]:
        flag = False
if flag:
    print('YES')
else:
    print('NO')


# s = input()
#
# if s == s[::-1]:
#     print("YES")
# else:
#     print("NO")
