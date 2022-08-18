# coding=utf-8
# 常用高阶函数
'''
def func1(x,y,f):
    return f(x) + f(y)
num = func1(-10, 2, abs)
print(num)
'''

# map  映射函数
#    一般来说接受两个函数，第一个函数使用作用的函数，第二个参数是要作用的可迭代对象
#    返回值是一个迭代器
'''
lst = [1, 2, 3, 4, 5, 6, 7]
lst2 = [10, 100, 1000, 10000]


def f1(x, y):
    return x + y


# map后面可以接受多个可迭代对象，那传入几个可迭代对象，前面的函数就要接受几个参数
# print(map(f1,lst,lst2))
print(list(map(f1, lst, lst2)))
print(list(map(lambda x, y: x + y, lst, lst2)))
'''


# filter   过滤函数
# filter的第一个参数传入一个函数，第二个参数是可迭代对象
# 将可迭代对象里的每一个值，交给传入的函数处理，如果结果为真，就保留这个值。
# 如果结果为假，就去掉这个值。
# filter也是返回一个迭代器
'''
print(list(filter(lambda x : x % 2, [1,2,3,4,5,6,7,8,9])))
print(2%2==False)
'''

# sorted    排序函数
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
# 把一个序列中的字符串，忽略大小写排序
'''
list1=['bob','about','Zoo','Credit']
print(sorted(list1,key=lambda x:x.lower()))
print(sorted(list1,key=str.lower))

d1 = {"a":3,"b":4,"c":2,"d":5}
print(dict(sorted(d1.items(), key=lambda x:x[1])))
'''


from functools import reduce
s = [1,3,5,7,9]
print(reduce(lambda x,y:x*10+y, s))