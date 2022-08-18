print("Hello,World!")

print("Hello,Python!")

'''
多行注释
'''

# 单行注释

# python Python使用缩进来代表代码块，不需要使用大括号{}
# 同一个代码块必须包含相同的的缩进空格数
# 缩进不一致，就会导致运行错误
if True:
    print("true")
    # print("true2")
else:
    print("false")

# 多行语句
'''
Python通常是一行写完一条语句，若语句很长，可以使用\(反斜杠)来实现多行语句
'''
print("a boy can do everything for gils\
      he is just kidding \
      love must need...")

item_one = 1
item_two = 2
item_three = 3

total = item_one + \
        item_two + \
        item_three
print(total)

'''
在[],{},()中的多行语句，不需要使用反斜杠 \
'''
total01 = ['item_one','item_two',
           'item_three']
print(total01)

#python 中数字（Number）只有四种类型
'''
整数：(int)  1
布尔型：(bool)   true
浮点型：(float)   1.23
复数：(complex)   1+2j
'''

#字符串（String）
'''
python中单引号和双引号的作用完全相同
转义符 \，使用r可以让斜杠不发生转义
索引方式：
    从左往右以0开始
    从右往左以-1开始
Python中的字符串不能改变
Python中没有单独的字符类型，一个字符就是长度为1的字符串
字符串截取格式：变量[头下标:尾下标:步长]
'''

str = '123456'

print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str[1:5:2])
print(str*2)
print(str+'你好')

print('hello\nrunoob')
print(r'hello\nrunoob')





