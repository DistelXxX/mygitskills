# coding=gbk
import time
from selenium.webdriver.common.by import By

from selenium import webdriver

driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.get("http://127.0.0.1:8848/UI_AUTO_TEST/index.html")
driver.get("http://localhost:8080/EasyBuy/Login?action=toLogin")

# ͨ��id��λԪ��
# driver.find_element(by=By.ID,value="kw").send_keys("China")

# ͨ��name��λԪ��
# driver.find_element(by=By.NAME,value="wd").send_keys("China")

# ͨ��class_name��λԪ��
# driver.find_element(by=By.CLASS_NAME,value="s_ipt").send_keys("China")

# ͨ��tag_name��λԪ��(����ʹ��tag_name����λ����Ԫ��)
# driver.find_element(by=By.TAG_NAME,value="input").send_keys("China")

# ͨ��link_text����ȫ�����ֶ�λԪ��
# driver.find_element(by=By.LINK_TEXT,value="����").click()

# ͨ��partial_link_text���Ӳ������ֶ�λԪ��
# driver.find_element(by=By.PARTIAL_LINK_TEXT,value="��").click()

# ʹ��XPATH��λԪ�أ�F12����>��λԪ�ء���>copy path��
# driver.find_element(by=By.XPATH,value='//*[@id="kw"]').send_keys("China")

# ʹ��CSS��λԪ�أ�F12����>��λԪ�ء���>copy selector��
# driver.find_element(by=By.CSS_SELECTOR,value='#kw').send_keys("China")

# ʹ��find_element('locator', 'value')��λԪ��
# (1)ֱ�Ӵ���
# driver.find_element('id','kw').send_keys("China")

# ��λ��Ԫ��find_elements
# els = driver.find_elements(by=By.TAG_NAME, value="input")
# print(len(els))
# els[7].send_keys("China")

#xpath��ϸʹ��
# ��1����������
# driver.find_element(by=By.ID,value='s_kw_wrap').find_element(by=By.TAG_NAME,value='input').send_keys("�й�")
# ��2��ͨ����Ԫ�ز�����Ԫ��
# driver.find_element(By.XPATH,'//form[@id="form"]/span/input').send_keys("�й�")
# ��3������xpath�ᣬͨ����Ԫ�ض�λ��Ԫ��
# driver.find_element(By.XPATH,'//form[@id="form"]/child::span/input').send_keys("�й�")
# ��4������Ԫ�ض�λ��Ԫ��/parent::tag_name
# ��5��ͨ���ܵ�Ԫ�ض�λ���Ԫ��/preceding-sibling::tag_name
# ��6��ͨ�����Ԫ�ض�λ�ܵ�Ԫ��/following-sibling::tag_name
# ��7��ͨ��CSS selector����λҳ��Ԫ��
# driver.find_element(By.CSS_SELECTOR,'form > span > input').send_keys("�й�")

# text = driver.find_element(By.CSS_SELECTOR,'div#parent div:nth-child(2)').text
# print(text)

#selenium4�����ķ���
# ��1��

# time.sleep(3)
# driver.find_element(by=By.ID, value="su").click()

time.sleep(3)

driver.quit()