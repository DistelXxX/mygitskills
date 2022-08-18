# coding=utf-8

from selenium import webdriver
import time
import xlrd2
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

data = xlrd2.open_workbook(r"C:\code\demo01\selenium_test\data_separation\data\data_sep.xls")

table = data.sheet_by_name('Sheet1')

list = []

for i in range(0,table.nrows):
    list = table.row_values(i)
    break

print(list)

time.sleep(3)

driver.get(list[0])

time.sleep(3)

driver.find_element(By.ID,list[2]).send_keys(list[3])

driver.find_element(By.ID,list[5]).click()

for i in range(1,table.nrows):
    list = table.row_values(i)
    break

print(list)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,list[0]).click()
time.sleep(1)
driver.find_element(By.ID,list[1]).send_keys(int(list[2]))
driver.find_element(By.ID,list[3]).click()
