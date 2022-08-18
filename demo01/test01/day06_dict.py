#dictionary
mydict = {'name':'shuiche','sex':'male','age':18}

emptyDict = {}#创建空字典
print(emptyDict)

print("Length:",len(mydict))

emptyDict = dict()#dict()也可创建空字典
print(type(emptyDict))

#访问字典元素
print(mydict['name'])

#修改字典元素
print(mydict['age'])
mydict['age'] = 22
print(mydict['age'])

#添加元素
mydict['hobby'] = 'video games'
print(mydict)

#删除字典元素
del mydict['hobby']
print(mydict)

# del mydict  字典不存在
# print(mydict)


#字典内置函数&方法
print(len(mydict))
print(str(mydict))

# dict.clear(mydict)#删除字典中的所有元素
print(mydict)

#返回一个字典的浅复制
print(dict.copy(mydict))


