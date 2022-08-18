# Python字符格式化（%s）
age = 18
name = "laiyongjun"
print("%s今年%d岁"%(name,age))

'''
python三引号允许一个字符串跨多行，字符串也可以包含换行符，制表符以及其他字符
'''
para_str="""aaaaaaaaaaaaaa
bbbbbbbbbbbbb
TAB(\t)
ccccccccccccc[\n]
"""
print(para_str)

print('hello %s'%name)


#f-string格式化字符串以f开头，后面跟着字符串，字符串中的表达式用大括号
#括起来，他会将变量或表达式计算后的值替换进去
# print(f'{1+2}')
# print(f'hello {name}')













