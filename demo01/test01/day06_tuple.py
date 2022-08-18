#tuple
tuple1 = ('Google','Runoob',1,3.4)
tuple2 = 'a','b','c','d','e';#不需要括号也可以
print(type(tuple2))

#创建空元组
tuple3 = ()
print(tuple3)

tuple4 = (20)
tuple5 = (20,)

print(type(tuple4))#单个元素不加逗号，此时tuple的类型为整型
print(type(tuple5))#单个元素不加逗号，此时tuple的类型为tuple

print(tuple1[0])
print(tuple1[1:3])

#修改元组
print(tuple1[1])
# tuple1[1] = 'baidu'---->修改元组元素是非法的
print(tuple1[1])

#创建新元组
tuple6 = tuple1 + tuple2
print(tuple6)

#删除元组
del tuple6
# print(tuple6)

#元组运算符
print(len(tuple1))
print(tuple2*2)
print('a' in tuple2)

for x in tuple2:
    print(x,end=" ")
print()

#内置函数
#len(),max(),min()

list1 = [1,2,3,4]
tuple7 = tuple(list1)#将可迭代列表转换为元组
print(type(tuple7))

list2 = list(tuple7)
print(type(list2))