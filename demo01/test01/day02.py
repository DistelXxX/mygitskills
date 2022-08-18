#可在同一行中写多条语句，yi;分号分割
import sys;x = 'runoob';sys.stdout.write(x + '\n')

x = "a"
y = "b"
#换行输出
print(x)
print(y)

print("===================")
#不换行输出
print(x, end=" ")
print(y, end=" ")
print()

#import 与 from...import...
'''
import:导入整个模块
from...import...:从某个模块中导入某个函数
'''

import sys
print("======================Python import mode========================")
print("命令行参数为：")
for i in sys.argv:
    print(i)
print('\npython 路径为',sys.path)

from sys import argv,path
print("======================Python from import========================")
print('path',path)

#python的数据类型，声明变量
counter = 100
miles = 1000.0
name = "赖永军"

print(counter)
print(miles)
print(name)

#同时为多个变量赋值
a = b = c = d = 1
print(a,b,c,d)

#分别赋值
a,b,c = 1,2,'runoob'
print(a,b,c)

#标准数据类型
'''
不可变数组：
    Number(数字)
        int(长整型),float,bool,complex
    String(字符串)
    Tuple(元组)
可变数组：
    List(列表)
    Set(集合)
    Dictionary(字典)
'''

#Number(数字)

a,b,c,d = 20, 5.5, True, 4+3j
#type(变量名):查看变量的数据类型
print(type(a),type(b),type(c),type(d))
#isinstance(变量名，猜测的数据类型)，判断结果为True或False
print(isinstance(a,int))

'''
两者区别：
    type()不会认为子类是一种父类类型
    isinstance()会认为子类是一种父类类型
'''
'''
注意:
    Python3中，bool是int的子类，True和False可以和数字相加
    True==1、False==0 会返回True
    但可以通过is来判断类型
'''

print(True==1)
print(True+1)
print(1 is True)

var1 = 1
print(var1)
# del var1
# print(var1)

'''
一个变量可以通过赋值指向不同类型的对象
数值的除法包含两个运算符：/返回一个浮点数；//返回一个整数
在混合计算时，Python会把整型转换成浮点数
'''

print(2/4)
print(2//4)
print(0.5*3)


#String(字符串)

'''
变量[头下标:尾下标]
索引值以0开始，-1为末尾的开始位置
'''

'''
字符串可以通过*加上数字重复字符串
Python中的字符串不能改变
'''

# word = 'python'
# print(word)
# word[0] = 'k'
# print(word)


#List(列表)

'''
列表中元素可以不相同
'''

list= ['a','b','c','d','e']
slist = ['f','g']

print(list)
print(list[0])
print(list[0:2])
print(list+slist)

# Tuple（元组）

'''
元素不能修改，元素可以不相同
'''

tuple = ('abcd',786,2.23,'noob',7.22)
tinytuple = (123,'runoob')

# print(tuple)
# print(tuple[0])
# print(tuple[1,2])
print(tuple[2:])
print(tinytuple*2)
print(tuple+tinytuple)

tup1 = ()#空元组
tup2 = (2,)#一个元素，需要在元素后接逗号','

'''
String,List,Tuple都属于sequence（序列）
'''















