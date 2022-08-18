#coding=utf-8
# 获取页面元素的相关信息
from selenium.webdriver.common.by import By

from selenium import webdriver
import time

driver = webdriver.Chrome()

# driver.get("https://www.baidu.com")
# ele = driver.find_element(By.LINK_TEXT,"新闻")
# print(ele.tag_name)#获取元素标签名
# print(ele.text)#获取元素文本
# print(ele.size)#获取元素大小
#
#
# ele1 = driver.find_element(By.ID,"kw")
# ele2 = driver.find_element(By.ID,"su")
#
# print(ele1.get_attribute("id"))
# print(ele2.get_attribute("id"))
# print(ele2.get_attribute("value"))
# print(ele1.get_attribute("value"))
# print(type(ele1.get_attribute("name")))
#
# print(ele.value_of_css_property("height"))
# print(ele.value_of_css_property("width"))
# print(ele.value_of_css_property("font-family"))

'''
判断页面元素是否可见
'''
# driver.get("http://127.0.0.1:8848/UI_AUTO_TEST/test01.html")
#
# ele1 = driver.find_element(By.ID,'div1')
# ele2 = driver.find_element(By.ID,'div2')
# ele3 = driver.find_element(By.ID,'div3')
# ele4 = driver.find_element(By.ID,'div4')
#
# print("ele1 is display:{}".format(ele1.is_displayed()))
# print("ele2 is display:{}".format(ele2.is_displayed()))
# print("ele3 is display:{}".format(ele3.is_displayed()))
# print("ele4 is display:{}".format(ele4.is_displayed()))
#
# driver.find_element(By.ID,"button1").click()
# driver.find_element(By.ID,"button2").click()
# print("++++++++++++++++++++++++++切换后+++++++++++++++++++++++++++")
# print("ele1 is display:{}".format(ele1.is_displayed()))
# print("ele2 is display:{}".format(ele2.is_displayed()))
# print("ele3 is display:{}".format(ele3.is_displayed()))
# print("ele4 is display:{}".format(ele4.is_displayed()))

'''
判断元素是否可用
'''

driver.get("http://127.0.0.1:8848/UI_AUTO_TEST/test02.html")

ele1 = driver.find_element(By.ID,'input1')
ele2 = driver.find_element(By.ID,'input2')
ele3 = driver.find_element(By.ID,'input3')

print("ele1 is enabled:{}".format(ele1.is_enabled()))
print("ele2 is enabled:{}".format(ele2.is_enabled()))
print("ele3 is enabled:{}".format(ele3.is_enabled()))

time.sleep(3)
driver.quit()
