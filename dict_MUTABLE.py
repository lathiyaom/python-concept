a = {"x": 1}
b = a
print(id(a), id(b))
a["y"] = 2
print(a, b)
print(id(a), id(b))
