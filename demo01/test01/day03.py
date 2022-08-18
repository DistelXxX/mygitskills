# Set（集合）

'''
基本功能是进行成员关系测试和删除重复元素
可以使用大括号{}或者set()函数创建集合
创建一个空集合必须使用set()而不是{}
{}是用来创建一个空字典
'''

sites = {'hello', 'test', 'world', 'runoob', 'runoob'}
print(sites)  # 去掉重复元素

# 成员测试
if 'test' in sites:
    print('test在集合中')
else:
    print('test不在集合中')

# set可以进行集合运算
a = set('asdhkjasdiqdl')
b = set('adsiqaksalsd')
print(a)
print(a - b)#差集
print(a | b)#并集
print(a & b)#交集
print(a ^ b)#不同时存在的元素

print("========================================================")
#Dictionary(字典)

'''
内置数据类型
列表是有序的对象集合，字典是无序的对象集合
区别：字典当中的元素是通过键来存取的，而不是通过偏移存取
字典的是一种映射类型，字典是用{}标识，是一个无需的键(key):值(value)的集合
键(key)必须使用不可变类型
同一个字典中，键(key)必须是唯一的
'''
dict = {}
dict['one'] = "1-开发"
dict[2] = "2 -测试"

tinydict = {'name': 'runoob','code':1,'site':'www.runoob.com'}


print(dict['one']) #输出键为‘one’的值
print(dict[2]) #输出键为‘2’的值
print(tinydict) #输出完整的字典
print(tinydict.keys()) #输出所有键
print(tinydict.values()) #输出所有值

print("==================================================")
#Python数据类型转换


'''
隐式数据类型转换-自动完成
显示数据类型转换-需要使用函数来转换
'''

num_int = 123
num_float = 1.23

num_sum = num_int + num_float#完成自动类型转换

print(num_sum)
print(type(num_sum))
#python会将较小的数据类型转换为较大的数据类型，以避免数据丢失

num_str = '456'

print(type(num_str))

# print(num_int+num_str)
#TypeError


#显示数据类型转换


#转换为整型
x1 = int(1.2)
x2 = int(1)
x3 = int("3")
print(x1)
print(x3)

#转换为浮点型
y1 = float(1)
y2 = float(2.8)
y3 = float("2.3")
print(y1)#数据类型已转换
print(y3)

#转换为字符串类型
z1 = str(1)
z2 = str(2.3)
z3 = str("s1")
print(type(z1))
print(type(z2))

#整型和字符串类型之间的运算可以通过强制类型；来转换完成

num_string = int (num_str)

print(num_int+num_str)
print(type(num_int+num_str))
