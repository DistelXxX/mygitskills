
# handle句柄
import time
from selenium.webdriver.common.by import By

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#获取当前窗口的句柄
print(driver.current_window_handle)

driver.find_element(by=By.LINK_TEXT, value="新闻").click()
#获取全部窗口的句柄
print(driver.window_handles)
all_handles = driver.window_handles

#切换句柄
driver.switch_to.window(all_handles[1])
time.sleep(2)
# driver.switch_to.frame(0)
# time.sleep(5)

# driver.switch_to.new_window("window")
time.sleep(2)
driver.close()

print(driver.window_handles)

time.sleep(5)
driver.quit()