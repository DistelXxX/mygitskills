# coding=utf-8
from selenium import webdriver
import time
import xlrd2
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 读取文件
data = xlrd2.open_workbook(r"C:\code\demo01\selenium_test\data_separation\data\data_sep.xls")
# 读取第一个工作表
table = data.sheet_by_name('Sheet1')
# 使用for循环输出所有数据
list = []
for i in range(2, table.nrows):
    # 只读取其中一行
    list = table.row_values(i)
    break
print(list)
# 判断是否有网址需要打开
if str(list[0]) != '':
    driver.get(list[0])
# 判断执行关键字
if str(list[1]) == u'输入数据':
    if list[2] == 'id':
        driver.find_element(By.ID,list[3]).send_keys(list[4])
time.sleep(3)
if str(list[5]) == u'点击搜索':
    if list[6] == 'id':
        driver.find_element(By.ID,list[7]).click()
time.sleep(3)
driver.close()
