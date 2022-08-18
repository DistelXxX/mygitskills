# 推导式

"""
推导式是一种独特的数据处理方式
可以从一个数据序列构建另一个新的数据序列的结构体
    列表（list）推导式
    字典（dict）推导式
    集合（set）推导式
    元组（tuple）推导式
"""

'''
列表推导式
'''

# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母
names = ['bob', 'tom', 'alice', 'jerry', 'wendy', 'smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

# 计算30以内可以被整除的整数
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

'''
字典推导式
'''

# 使用字符串及其长度创建字典
listdemo = ['Google', 'Runoob', 'Taobao']
newdict = {key: len(key) for key in listdemo}
# 列表中各字符串值为键，各字符串的长度为值
print(newdict)

# 提供三个数字，以三个数字为键，三个数的平方为值来创建字典
dic = {x: x ** 2 for x in (1, 2, 4)}
print(dic)

'''
集合推导式
'''

# 计算数字1,2,3的平方数
setnew = {i ** 2 for i in (1, 2, 3)}
print(setnew)

# 判断不是abc的字母并输出
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

'''
元组推导式
'''

# 生成一个包含数字1~9的元组
a = (x for x in range(1, 10))
print(a)  # 返回一个生成器对象
print(tuple(a))

'''
python位运算符
'''

# a = 0011 1100
# b = 0000 1101
#
# print(a&b)

a = 60
b = 13
c = 0

c = a & b
# 二进制按位运算
print(c)
# 逻辑运算（布尔值）
print(a and b)

i = 1
n = '*'
while i <= 50:
    print(n * i)
    i += 1

for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print("%d*%d=%-2d" % (i, j, i * j), end=" ")
    print("\n")

print("请输入用户名：")
a_name = input()
print(a_name)
print("请输入密码：")
a_passwd = input()  # 123

while a_name != 'lyj':
    print("用户名错误，请重新输入：")
    print("用户名：", end=" ")
    a_name = input()
    print()
    if a_name != 'lyj':
        continue
    print("密码：", end=" ")
    a_passwd = input()
    break
while a_passwd != '123':
    print("密码错误，请重新输入：")
    a_passwd = input()
print("登录成功")
