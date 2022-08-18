# 鼠标单击操作
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.get("http://sahitest.com/demo/")
# driver.get("http://sahitest.com/demo/formTest.htm")
# driver.get("http://localhost:8080/EasyBuy/Login?action=toLogin")
# driver.get("file:///C:/Users/Administrator/Downloads/runoob-tryjsref_ondrop.html")
driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
'''
driver.find_element(By.ID, "kw").send_keys("China")
driver.find_element(By.ID, "su").click()
'''
'''
鼠标双击操作
'''
# ele = driver.find_element(By.XPATH, '/html/body/form/input[2]')
# ActionChains(driver).double_click(ele).perform()

'''
鼠标右击操作
'''

# ele = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/a[2]')
# ActionChains(driver).context_click(ele).perform()

'''
鼠标悬停操作
'''
# ele = driver.find_element(By.CLASS_NAME, 's_city')
# ActionChains(driver).move_to_element(ele).perform()

'''
鼠标拖动操作
'''
# ele1 = driver.find_element(By.XPATH,'//*[@id="dragtarget"]')
# ele2 = driver.find_element(By.CLASS_NAME,'droptarget')

# source = driver.find_element(By.XPATH,'//*[@id="dragger"]')
# target = driver.find_element(By.XPATH,'/html/body/div[2]')
# ActionChains(driver).drag_and_drop(source,target).perform()


time.sleep(3)
driver.quit()
