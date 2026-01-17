a = (1, 2)
b = a
print(id(a), id(b))

a = a + (3,)
print(a, b)
print(id(a), id(b))
