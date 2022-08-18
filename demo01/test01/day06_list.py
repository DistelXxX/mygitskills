'''
list
tuple
dictionary
set
'''

# list
list1 = ['Google', 'Runoob', 1997, 2000]  # 元素可以是不同的数据类型

# 列表的索引
print(list1[0])
print(list1[1])

print(list1[-1])
print(list1[-2])

# 列表的片段截取(左开右闭)
print(list1[1:3])
print(list1[1:-1])

# 更新列表
print(list1[2])
list1[2] = 2008
print(list1[2])

list1.append(2012)
print(list1)

#删除列表元素
del list1[-1]
print(list1)

#列表脚本操作符
print(len(list1))#求列表长度
num1 = [1,2,3]
num2 = [4,5,6]
print(num1+num2)#组合列表
print(num1*4)#重复列表

for x in num1:
    print(x,end="")#迭代列表元素

#列表比较（导入operator）
import operator
a = [1,2]
b = [3,4]
c = [5,6]
print()
print(operator.eq(a,b))

#列表函数&方法
print(max(num2))
print(min(num2))
print(len(num2))
print(num1.index(1))

print(2 in num1)
num1.append(1)
print(num1.count(1))

#追加扩展列表
num3 = list(range(7,10))
num2.extend(num3)
print(num2)

#移除列表中的一个元素，默认最后一个，并返回该元素的值
# print(num1.pop())
num1.remove(1)
print(num1)

num2.reverse()
print(num2)

num1.sort()
print(num1)

num3.clear()
print(len(num3))

num3 = num1.copy()
print(num3)









