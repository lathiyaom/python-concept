# nums = [1, 2, 3]
# for x in nums:
#     x += 1
# print(nums)
#
# lists = [[1], [2], [3]]
# for x in lists:
#     x.append(90)
# print(lists)
import copy


# list = [[1], [2], [3]]
# for i in range(len(list)):
#     list[i] = list[i] + [0]
#
# print(list)
# a = [[1, 2], [3, 4]]
#
# for i in range(len(a)):
#     a[i] = a[i] + [99]
#
# print(a)

# s = ""
# for i in range(5):
#     s = s + str(i)
# print(type(s))

# parts = []
#
# for i in range(5):
#     parts.append(str(i))
# s = "".join(parts)
#
# print(s)

# def add_suffix(s):
#     return s + "_end"
#
#
# x = "data"
# x = add_suffix(x)
# print(x)
# class Person:
#     pass
#
#
# p = Person()
# print(p)  # <__main__.Person object at ...>


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)

    def greet(self):
        print("Hello,My name is ,", self.name)


u = User("BOB", 10)
# u.mark = 120
# print(u.age)
# print(u.name)
# print(u.mark)
u.greet()
