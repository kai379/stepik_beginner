# Шифр Цезаря
# 97 - a   122 - z   25

num_shift = int(input())
s = input()
decode = ''
for i in range(len(s)):
    char_el = s[i]
    if ord(char_el) - num_shift >= ord('a'):
        char_el = chr(ord(char_el) - num_shift)
    else:
        char_el = chr(ord('z') - (num_shift - (ord(char_el) - ord('a') - 1)))
    decode += char_el

print(decode)

