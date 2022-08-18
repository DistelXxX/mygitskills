#coding=utf-8
#给你一个字符串“hello_world_lyj”,如何得到一个队列['hello','world','lyj']
"""
str01 = 'hello_world_lyj'
print(str01.split("_"))
"""

#将列表['hello','world','lyj']中的元素用‘_’连起来
'''
list01 = ['hello','world','lyj']
print("_".join(list01))

list02 = ""
for i in list01:
    list02 += i
print(list02)
'''

# 把字符串 s 中的每个空格替换成”%20”
# 输入：s = “We are happy.”
# 输出：”We%20are%20happy.”
'''
s = "we are happy"
print(s.replace(" ","%20"))
'''

#打印99乘法口诀表
# for i in range(1,10):
#     for j in range(1,10):
#         if j <= i:
#             # print("%d*%d=%-3d"%(i,j,i*j),end="")
#             print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()
'''
i = 1
while i<=9:
    j = 1
    while j<=i:
        print('{}x{}={}\t'.format(j, i, i*j), end='')
        j += 1
    i += 1
    print()
'''

# 找出单词 “welcome” 在 字符串”Hello, welcome to my world.” 中出现的位置，找不到返回-1
# 从下标0开始索引
'''
def test():
    str01 = "welcome"
    str02 = "hello, welcome to my world"

    if str01 in str02:
        return str02.find(str01)
    else:
        return -1
print(test())
'''

# 统计字符串“Hello, welcome to my world.” 中字母w出现的次数
# 统计单词 my 出现的次数
'''
str01 = "hello, welcome to my world"
print(str01.count("w"))
'''

# 题目:输入一个字符串str, 输出第m个只出现过n次的字符，如在字符串 gbgkkdehh 中,
# 找出第2个只出现1 次的字符，输出结果：d
'''
str01 = input('请输入一个字符串：')
# dict01 = {}
list01 = []
for i in str01:
    count = str01.count(i)
    if count == 1:
        list01.append(i)
print(list01[1])
'''

# 判断字符串a=”welcome to my world” 是否包含单词b=”world”
# 包含返回True，不包含返回 False
'''
a = 'welcome to my world'
b = 'world'

def test():
    if b in a :
        return True
    else:
        return False

print(test())
'''

# 输出指定字符串A在字符串B中第一次出现的位置,如果B中不包含A,则输出-1
# 从 0 开始计数
'''
A = 'hello'
B = 'hi how are you hello world, hello yoyo !'

def test():
    if A in B:
        index = B.find(A)
        return index
    else:
        return -1

index = test()
print(index)
'''

# 输出指定字符串A在字符串B中最后出现的位置,如果B中不包含A, 出-1从 0 开始计数
# A = “hello”
# B = “hi how are you hello world, hello yoyo !”
'''
A = 'hello'
B = 'hi how are you hello world, hello yoyo !'

def test():
    if A in B:
        index = B.rfind(A)
        return index
    else:
        return -1

print(test())
'''

# 给定一个数a，判断一个数字是否为奇数或偶数
# a1 = 13
# a2 = 10
'''
a1 = 13
a2 = 10

if a1 % 2 == 1:
    print("%d为奇数"%a1)
elif a1 % 2 == 2:
    print("%d为偶数"%a1)
'''
'''
while True:
    try:
        a =int(input("请输入一个整数："))
    except ValueError:
        print("输入的不是整数")
        continue
    if a % 2 == 0:
        print("%d为偶数"%a)
        break
    else:
        print("%d为奇数"%a)
'''


# 输入一个姓名，判断是否姓王
# a = “王五”
# b = “老王”
'''
while True:
    name = input("请输入一个姓名：")
    if name[0] == '王':
        print("他姓王")
        break
    else:
        print("他不姓王")
'''

# 如何判断一个字符串是不是纯数字组成
# a = “123456”
# b = “yoyo123”

'''
def isNum(num):
    try:
        num = float(num)
        print("是纯数字")
    except Exception as e:
        print("不是纯数字")

isNum("12345")
'''

#通过range函数生成奇数偶数列表

'''
#方法一
list1 = [i for i in range(1,20,2)]
print(list1)

#方法二
a = list(range(1,20,2))
print(a)
'''

#python1234组成不同三位数-python输出由1,2,3,4组成
#的互不相同且无重复的三位数
'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (i!=k) and (j!=k):
                print(str(i)+str(j)+str(k))
'''

#冒泡排序
'''
array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]

for i in range(0,len(array)-1):
    for j in range(0,len(array)-1):
        if array[j] > array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]
print(array)
'''

#乘法口诀表
'''
for x in range(1,10):
    for y in range(1,x+1):
        #end=" "意思是末尾不换行，加空格
        print("%s*%s=%s" % (y,x,x*y),end=" ")
    print("")
'''

# 将字符串转换大小写
'''
a = 'a boy can do everything for girl'
b = 'HE IS JUST KIDDING'

print(a.upper())
print(b.lower())
'''

#python提供了strip()方法，可以去除首尾空格
#rstrip()去掉尾部空格
#lstrip()去掉首部空格
#replace(" ","")去掉全部空格
'''
a = ' a boy can do everything for girl '
print(a.strip())
print(a.rstrip())
print(a.lstrip())
print(a.replace(" ",""))
'''

#递归方式去掉空格
'''
def trim(s):
    flag = 0
    if s[:1]==' ':
        s = s[1:]
        print(s)
        flag = 1
    if s[-1:] == ' ':
        s = s[:-1]
        print(s)
        flag = 1
    if flag==1:
        return    trim(s)
    else:
        return s
print(trim('  Hello world!  '))
'''

#s = “ajldjlajfdljfddd”，去重并从小到大排序输出”adfjl”
'''
s = "ajldjlajfdljfddd"
s = list(s)
print(s)
s = set(s)
s = list(s)
s.sort()
s = "".join(s)
print(s)
'''

'''
def test():
    s = "ajldjlajfdljfddd"
    list01 = []
    for i in s:
        if i in list01:
            list01.remove(i)
        list01.append(i)
    a = sorted(list01)

    return "".join(a)

print(test())
'''

# 题目 给一个不多于5位的正整数，要求：
# 一、求它是几位数，
# 二、逆序打印出各位数字。
# a = 12345
'''
def method(a):
    a = str(a)
    print("位数："+len(a))
    a = list(a)
    a.reverse()
    for i in a:
        print(i)
method(123)
'''

# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
# 例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
# 那么问题来了，求1000以内的水仙花数（3位数）
'''
def test():
    for num in range(100,1000):
        i = num//100
        j = num//10%10
        k = num%10

        if i ** 3 + j ** 3 + k ** 3 == num:
            print(str(num)+"是水仙花数")
test()
'''

