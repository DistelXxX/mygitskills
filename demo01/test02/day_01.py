# coding=utf-8

# 多行字符串
strs = """黑云压城城欲摧，
甲光向日金鳞开。"""
print(strs)
print(id(strs))

strs = "abc"
print(id(strs))
# 字符串str不能改变内容，对字符串进行更改是字符串变量的地址指向发生了改变
s = '1234567890'

#正向
print(s[1:5])#输出下标为2~4的字符
print(s[1])
print(s[1:])
#反向
print(s[2:-1])

print("123\n456")
print(r"123\n456")#加”r“不发生转义


input("\n\n按下 enter 键后退出。")



