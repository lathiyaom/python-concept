# import copy
#
# a = [[1, 2, 3], [4, 5, 6]]
# b = copy.deepcopy(a)
# b[1].append(99)
# print(a)
# print(b)
# matrix = [[0] * 3] * 3
# matrix[0] = 1
# print(matrix)

# def add_item(lst):
#     lst.append(1)
#
#
# x = []
# add_item(x)
#
# print(x)
# a = [[1, 2], [3, 4]]
# b = a.copy()
#
# b[1].append(99)
#
# print(a)
# print(b)
# def collect(x, result=None):
#     if (result is None):
#         result = []
#     result.append(x)
#     return result
#
#
# print(collect(1))
# print(collect(2))
# print(collect(3))
a = [1, 2]
b = a
c = a[:]
b.append(3)

print(a)
print(b)
print(c)
