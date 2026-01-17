# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(a)
# print(b)

a = [[1, 2, 3], [4, 5, 6]]
b = a.copy()
b[0].append(99)
print(a)
print(b)
