# set集合
myset = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
print(myset)

a = set('adfghjkl')
b = set('ghjkl')

# 两个集合间的运算
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

#添加元素
myset.add('h')
print(myset)

myset.update('i')
print(myset)

#移除元素
myset.remove('i')#无该元素，报错
print(myset)

myset.discard('h')
print(myset)

#随机删除一个元素
myset.pop()
print(myset)

