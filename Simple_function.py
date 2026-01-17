def add_one(x):
    print(id(x))
    x = x + 1
    print(id(x))


a = 10
add_one(a)
print(id(a))
