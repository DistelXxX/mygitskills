

"""
csv文件读写
csv：逗号分隔值，是个纯文本文件，通常用来存储测试数据
"""

# import csv
#
# #newline = ''解决每次写入多一个空行的问题
# with open('study1.csv', 'a',newline='') as file1:
#     obj = csv.writer(file1)
#     # obj.writerow(['3','wangwu','18'])#向csv文件写入一行记录
#     obj.writerow(['4','赵六','14'])
#
#
# #读
# with open('study1.csv','r') as file2:
#     obj = csv.reader(file2)
#     for i in obj:
#         print(i)

"""
excel文件读写
1、先安装pip install xlrd2（cmd命令）
"""

# import xlrd2
#
# def read_excel(file_name,index):
#     excel = xlrd2.open_workbook(file_name)#打开一个excel文件
#     sheet = excel.sheets()[index]
#     return sheet
#
# if __name__ == '__main__':
#     # table = read_excel('study1.xlsx',0)#得到索引为0的sheet
#     # table = read_excel('./data/study1.xlsx',0)#相对路径
#     # table = read_excel(r'C:\code\demo01\test01\data\study1.xlsx',0)#反斜杠\代表转义，加上r的话相当于不转义，原样输出
#     # table = read_excel('C:\\code\\demo01\\test01\\data\\study1.xlsx',0)#绝对路径，不推荐
#     table = read_excel('C:/code/demo01/test01/data/study1.xlsx',0)#绝对路径，不推荐
#     for i in range(1,table.nrows):#table.nrows返的是行数
#         rows = table.row_values(i)#得到指定行的内容，以列表形式返回
#         print(rows)
#         print(rows[1])

"""
xml文件读写
xml：可标记扩展语言，通常用来做配置文件
读：方式1:DOM,文档对象模型
"""

#读：方式1：DOM，文档对象模型（document object model）
import xml.etree.ElementTree as ET
def read_xml(file_name,node_name):
    datas = []#定义一个空列表，用来存储指定节点的内容
    tree = ET.parse(file_name)#得到元素树
    root = tree.getroot()#得到根
    # print(root)根目录config
    for i in root.iter(node_name):#循环遍历指定名称的所有节点
        datas.append(i.text)#将匹配的节点值加入列表
    return datas
if __name__ == '__main__':
    result = read_xml('./data/study1.xml','username')
    print(result[0])
    print(result[1])
    print(result)



























