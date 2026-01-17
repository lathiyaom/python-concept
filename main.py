a = [1, 2]
b = a

print(id(a), id(b))

a.append(4)

print(id(a), id(b))
print(a)
