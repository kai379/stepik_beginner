n = int(input())

for i in range(n):
    s = input()
    if s.isspace() or s == '':
        print(f'{i + 1}: COMMENT SHOULD BE DELETED')
    else:
        print(str(i + 1) + ': ' + s)
