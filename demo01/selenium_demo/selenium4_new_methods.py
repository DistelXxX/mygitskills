#coding=utf-8
#selenium4新增的方法
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.relative_locator import with_tag_name

import time

driver = webdriver.Chrome()
# driver.get("http://localhost:8080/EasyBuy/Login?action=toLogin")
driver.get("http://localhost:8080/EasyBuy/")

# passwordField = driver.find_element(By.ID,'password')
# passwordField.send_keys("123456")
# # 定位id为password的iuput框上面的input框
# driver.find_element(with_tag_name('input').above(passwordField)).send_keys("admin")
# # 定位id为password的iuput框下面的input框
# driver.find_element(with_tag_name('input').below(passwordField)).click()

field1 = driver.find_element(By.LINK_TEXT,'登录')
text = field1.text
print(text)
# field1.click()
# 右边
# driver.find_element(with_tag_name('a').to_right_of(field1)).click()
# 附近不大于50像素的距离
driver.find_element(with_tag_name('a').near(field1)).click()
time.sleep(5)

driver.quit()