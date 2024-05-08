s = input()
count = 0
for i in s:
    if i == i.lower() and i.lower() in 'abcdefghijklmnopqrstuvwxyz':
        count += 1
print(count)

# print(sum(s.islower() for s in input()))

# s = input()
# cnt = 0
# for ch in s:
#     if 'a' <= ch <='z': cnt+=1
# print(cnt)

# s = input()
# cnt_al_lower = 0
#
# for el in s:
#     if el != el.upper():
#         cnt_al_lower += 1
#
# print(cnt_al_lower)

# s = input()
# count = 0
# for i in range(len(s)):
#     if s[i] in "abcdefghijklmnopqrstuvwxyz":
#         count+=1
# print(count)


