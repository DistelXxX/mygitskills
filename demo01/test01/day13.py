"""
文件——txt
"""

# #方式一：不推荐
# #以写的方式打开一个文件
# file1 = open('1.txt','w')
# #向文件中写入内容
# file1.write("我不爱你")
# #关闭以打开的文件
# file1.close()
#
#
#以读的方式打开一个文件
# file2 = open('1.txt','r')
# #读取文件的全部内容
# result = file2.read()
# #打印文件的内容
# print(result)
# file2.close()

# #方式二：推荐，读写完之后不需要写关闭语句，会自动关闭
# #文件打开模式：r（读），w（覆盖写），a（添加），b（二进制）
# #写的方式打开
# with open('1.txt','w') as file3:
#     file3.write("你问我爱你有多深")
# #追加的方式写入
# with open('1.txt','a') as file3:
#     file3.write("\n你问我爱你有多深")
# #写入的对象是列表
# with open('1.txt','a') as file3:
#     file3.writelines(['\n爱你有几分','\n爱你有几分'])

# #读
# with open('1.txt','r') as file4:
#     # result = file4.read()#读取所有内容
#     # result = file4.readline()#读取第一行
#     # result = file4.readlines()#读取所有行
#     result = file4.read().splitlines()#读取所有行，去掉所有换行符
#     print(result)

"""
定义读写方法
"""

