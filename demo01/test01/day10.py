"""
函数
"""

def hello():
    print("hello,world")

hello()

def triple_angle():
    for i in range(1,10):
        for j in range(1,10):
            if i>=j:
                print("%d*%d=%-4d"%(i,j,i*j),end="")
        print()

triple_angle()

def max(a,b):
    if a> b:
        return a
    else:
        return b
a = 4
b = 5

print(max(a,b))

def area(width,length):
    return width*length

width = 4
length = 5

print(area(width,length))

def printme(str):
    print(str)

printme("hello,world")

a = [1,3,4]
print(type(a))

a = 'runoob'
print(type(a))

def change(a):
    print(id(a))

    a = 10
    print(id(a))

a = 1
print(id(a))
change(a)

def changeList(mylist):
    mylist.append([1,2,3,4])
    print(mylist)
    return

mylist = [10,20,30]
changeList(mylist)
print(mylist)


#printinfo()不需要参数使用指定顺序
# def printinfo(name,age):
#     print("name:",name)
#     print("age:",age)
#     return
#
# printinfo(age='18',name='shuiche')

"""
不定长参数
加了星号*的参数会以元组的形式导入，存放未命名的变量参数
"""

'''
def printinfo(arg1,*vartuple):
    print("输出：")
    print(arg1)
    # print(*vartuple)
    # return
# printinfo(70,60,50)
    for var in vartuple:
        print(var)
    return

printinfo(10)#vartuple为空元组
printinfo(11,12,13)#arg1参数已被赋值，(11,12,13)传入vartuple元组中
'''


"""
加了两个星号**的参数会以字典的形式导入
"""
def printinfo(arg1,**vardict):
    print("输出：")
    print(arg1)
    print(vardict)

printinfo(1,a = 2,b = 3)


"""
*号可以单独出现，但是*后面的参数必须用关键字传入
"""

def f(a,b,*,c):
    return a+b+c
# f(1,2,3)
n = f(1,2,c=3)
print(n)

'''
匿名函数
lambda表达式
'''
x = lambda d,e:d+e
print(x(5,4))

def myFunc(n):
    return lambda a:a*n
mydoubler = myFunc(2)
mytripler = myFunc(3)

print(mydoubler(11))
print(mytripler(11))

















