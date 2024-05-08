a = 256
b = 257
print(id(a), id(b))

a += 1
print(id(a), id(b))

a = -256
b = -256
print(id(a), id(b))

# a -= 1
# print(id(a), id(b))
