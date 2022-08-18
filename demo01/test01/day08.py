'''
迭代器与生成器
'''

# 迭代器

"""
访问集合元素的一种方式
可以记住遍历的位置的对象
从第一个元素开始访问，到最后一个元素被访问结束，迭代器只能往前不会后退
基本方法：iter()和next()
"""

list1 = [1, 2, 3, 4, 5, 6]

it1 = iter(list1)
print(next(it1))  # 1
print(next(it1))  # 2
print(next(it1))  # 3
print(next(it1))  # 4
print(next(it1))  # 5
print(next(it1))  # 6

# for语句循环遍历
list2 = [1, 2, 3, 4, 5, 6]
it2 = iter(list2)
for x in it2:
    print(x, end=", ")

# 使用next()遍历循环
import sys

list3 = [1, 2, 3, 4, 5, 6]
it3 = iter(list3)
while True:
    try:
        print(next(it3))
    except StopIteration:  # 超出列表长度
        sys.exit()

# 面向对象
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
#
# myclass =MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# 生成器

'''
使用了yield的函数被称为生成器（generator）
生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
在调用生成器的过程中，每次遇到yield函数会暂停并保存当前所有的运行信息
返回yield的值，并在下一次执行next()方法时从当前位置继续运行
调用一个生成器函数，返回的是一个迭代器对象
'''

import sys


def fibonacci(n):  # 生成器函数
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)

while True:
    try:
        print(next(f), end="")

    except StopIteration:
        sys.exit()
