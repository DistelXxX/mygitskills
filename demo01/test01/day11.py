"""
列表是可变的，字符串和元组不能
"""

mylist1 = [1,2,3]
mylist2 = [4,5,6]

mylist2.append(7)
print(mylist2)

mylist1.extend(mylist2)
print(mylist1)

mylist1.insert(0,0)
print(mylist1)

mylist1.remove(7)
print(mylist1)

x = mylist1.pop(len(mylist1)-1)
print(x)
print(mylist1)

mylist2.clear()
print(mylist2)

y = mylist1.index(5)
print(y)

z = mylist1.count(1)
print(z)

mylist3 = [3,1,2]
mylist3.sort()
print(mylist3)

mylist3.reverse()
print(mylist3)

mylist4 = mylist3.copy()
print(mylist4)

'''
将列表作为堆栈使用
'''

stack = [3,4,5]

stack.append(6)
print(stack)

x1 = stack.pop()
print(x1)
print(stack)

'''
将列表作为队列使用
'''
from collections import deque
queue = deque(['a','b','c','d'])
queue.append('e')
queue.append('f')
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)


"""
列表推导式
"""
vec = [1,2,3]

aa = [x*2 for x in vec if x > 2]

print(aa)


#嵌套列表
martix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

bb = [[row[i] for row in martix] for i in range(4)]

print(bb)


transposed = []

for i in range(4):
    transposed.append(row[i] for row in martix)

print(transposed)

a = {x for x in 'asdfdsasdfdsaghjkl' if x not in 'asdf'}

print(a)

