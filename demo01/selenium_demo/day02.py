# coding = gbk
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(2)

# driver.get("https://i.csdn.net/")
# time.sleep(2)

# driver.back()
# time.sleep(2)
#
# driver.forward()
# time.sleep(2)
#
# driver.refresh()
# time.sleep(2)
#
driver.maximize_window()
time.sleep(2)

driver.minimize_window()
time.sleep(2)

driver.fullscreen_window()
time.sleep(2)

# winsize = driver.get_window_size()
# print(winsize)
#
# print(type(winsize))
# time.sleep(2)
#
# driver.set_window_size(800,500)
# time.sleep(2)

# winposition = driver.get_window_position()
# print(winposition)
#
# driver.set_window_position(20,20)
# time.sleep(2)

# title = driver.title
# print(title)

# currenturl = driver.current_url
# print(currenturl)

# page_source = driver.page_source
# print(page_source)

time.sleep(5)
driver.quit()

