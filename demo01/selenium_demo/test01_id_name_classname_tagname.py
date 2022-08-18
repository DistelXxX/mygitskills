# coding=gbk
import time
from selenium.webdriver.common.by import By

from selenium import webdriver

driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.get("http://127.0.0.1:8848/UI_AUTO_TEST/index.html")
driver.get("http://localhost:8080/EasyBuy/Login?action=toLogin")

# 通过id定位元素
# driver.find_element(by=By.ID,value="kw").send_keys("China")

# 通过name定位元素
# driver.find_element(by=By.NAME,value="wd").send_keys("China")

# 通过class_name定位元素
# driver.find_element(by=By.CLASS_NAME,value="s_ipt").send_keys("China")

# 通过tag_name定位元素(很少使用tag_name来定位单个元素)
# driver.find_element(by=By.TAG_NAME,value="input").send_keys("China")

# 通过link_text链接全部文字定位元素
# driver.find_element(by=By.LINK_TEXT,value="新闻").click()

# 通过partial_link_text链接部分文字定位元素
# driver.find_element(by=By.PARTIAL_LINK_TEXT,value="闻").click()

# 使用XPATH定位元素（F12——>定位元素——>copy path）
# driver.find_element(by=By.XPATH,value='//*[@id="kw"]').send_keys("China")

# 使用CSS定位元素（F12——>定位元素——>copy selector）
# driver.find_element(by=By.CSS_SELECTOR,value='#kw').send_keys("China")

# 使用find_element('locator', 'value')定位元素
# (1)直接传递
# driver.find_element('id','kw').send_keys("China")

# 定位组元素find_elements
# els = driver.find_elements(by=By.TAG_NAME, value="input")
# print(len(els))
# els[7].send_keys("China")

#xpath详细使用
# （1）串联查找
# driver.find_element(by=By.ID,value='s_kw_wrap').find_element(by=By.TAG_NAME,value='input').send_keys("中国")
# （2）通过父元素查找子元素
# driver.find_element(By.XPATH,'//form[@id="form"]/span/input').send_keys("中国")
# （3）借用xpath轴，通过父元素定位子元素
# driver.find_element(By.XPATH,'//form[@id="form"]/child::span/input').send_keys("中国")
# （4）由子元素定位父元素/parent::tag_name
# （5）通过弟弟元素定位哥哥元素/preceding-sibling::tag_name
# （6）通过哥哥元素定位弟弟元素/following-sibling::tag_name
# （7）通过CSS selector来定位页面元素
# driver.find_element(By.CSS_SELECTOR,'form > span > input').send_keys("中国")

# text = driver.find_element(By.CSS_SELECTOR,'div#parent div:nth-child(2)').text
# print(text)

#selenium4新增的方法
# （1）

# time.sleep(3)
# driver.find_element(by=By.ID, value="su").click()

time.sleep(3)

driver.quit()