s = input(). split()
s2 = []
for i in s:
    s2.append(int(i))
min_n = min(s2)
max_n = max(s2)
for i in range(len(s2)):
    if s2[i] == max_n:
        s2[i] = min_n
    elif s2[i] == min_n:
        s2[i] = max_n
print(*s2)
