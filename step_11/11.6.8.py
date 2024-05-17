n = int(input()[1:])
for _ in range(n):
    s = input()
    if '#' in s:
        print(s[:s.find('#')].rstrip())
    else:
        print(s)

# # put your python code here
# n = int(input()[1:])
#
# for i in range(n):
# 	line = input().split('#')
# 	line = line[0].rstrip()
# 	print(line)
