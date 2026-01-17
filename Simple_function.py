# def add_one(x):
#     print(id(x))
#     x = x + 1
#     print(id(x))
#
#
# a = 10
# add_one(a)
# print(id(a))


# def add_items(lst):
#     lst.append(10)
#
#
# a = []
# add_items(a)
# add_items(a)
# print(a)

# Bad coding
# def add_listItem(lst=[]):
#     lst.append(1)
#     return lst
#
#
# print(add_listItem())
# print(add_listItem())
# print(add_listItem())
# print(add_listItem())
# print(add_listItem())
# print(add_listItem())
# print(add_listItem())
#

# Good coding
# def add_itmes(lst=None):
#     if lst is None:
#         lst = []
#     lst.append(1)
#     return lst
#
#
# print(add_itmes())
# print(add_itmes())
# print(add_itmes())
# print(add_itmes())
def f(x, y=[]):
    y.append(x)
    return y


print(f(1))
print(f(2))
print(f(3))
