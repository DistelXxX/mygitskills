# 导入selenium
import time

from selenium.webdriver.common.by import By

from selenium import webdriver

# 实例化浏览器驱动对象（创建浏览器驱动对象）
driver = webdriver.Chrome()  # 创建谷歌浏览器驱动对象

# 打开网站
driver.get(
    "file:///C:/Users/Administrator/Desktop/python/ui自动化/pagetest/注册A.html")

# 通过元素的ID属性进行元素定位

'''
driver.find_element(by = By.ID,value="userA").send_keys("admin")
driver.find_element(by = By.ID,value="passwordA").send_keys("123456")
'''

# 通过元素的name属性值进行元素定位

'''
driver.find_element(by = By.NAME,value="userA").send_keys("admin")
driver.find_element(by = By.NAME,value="passwordA").send_keys("123456")
'''

# 通过class_name属性值进行元素定位

driver.find_element(by=By.CLASS_NAME, value="telA").send_keys("15970926681")
driver.find_element(by=By.CLASS_NAME, value="dzyxA").send_keys("911149062@qq.com")

# 等待3秒
time.sleep(10) # 导入time模块

# 退出浏览器驱动（释放系统资源）
driver.quit()
