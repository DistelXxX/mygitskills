# python编程第一步

# 斐波那契数列
'''
a,b = 0,1
while b < 10:
    print(b)
    a,b = b,a+b
'''
# end关键字
a, b = 0, 1
while b < 10:
    print(b, end=", ")
    a, b = b, a + b

# if...elif
# age = int(input("请输入您的年龄："))
# print("")
# if age <= 12:
#     print("少年！")
# elif (age > 12 and age <= 18):
#     print("青少年！")
# elif (age > 18 and age <= 40):
#     print("青年！")

#猜字游戏
number = 7
guess_num = -1;
while guess_num != number:
    guess_num = int(input("请重新输入猜测的数字："))
    if guess_num < number:
        print("您输入的数字小了！")
    elif guess_num > number:
        print("您输入的数字大了！")
    elif guess_num == number:
        print("您输入的数字正确！！！")

'''
循环语句for、while
'''

#计算1到100的总和

sum,a = 0,1

while a<=100:
    sum = sum + a
    a = a + 1
print("1到100的总和为：",sum)

#while...else
count = 0
while count < 5:
    print(count,"小于5")
    count = count + 1
else:
    print(count,"大于或等于5")

#while循环体中只有一条语句
# flag = 1
# while (flag): print("hello，world")
# print("goodbye")

"""
for语句
"""

#for语句实现1到100的总和
totalsum = 0
for x in range(1,101):
    totalsum = totalsum + x
print(totalsum)

#for循环遍历列表
list1 = ['a','b','c','d','e']
for y in list1:
    print(y,end=", ")

for y in list1:
    if y == list1[0]:
        print("[",y,end=', ')
    elif y == list1[len(list1)-1]:
        print(y,end=']')
    else:
        print(y,end=', ')

#range()函数左开右闭
#range(x,y,z)x,y为数据范围，z为增量步长
print()
for a1 in range(5,100,5):
    print(a1)

#结合range()和len()函数
list2 = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for a2 in range(len(list2)):
    print(a2,list1[a2])










