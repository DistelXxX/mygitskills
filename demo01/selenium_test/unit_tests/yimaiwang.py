# coding=utf-8
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver


class YMW:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get('http://localhost:8080/EasyBuy/')
        self.driver.maximize_window()
        time.sleep(1)

    def do_login(self):
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/span[2]/span/a[1]').click()
        time.sleep(2)
        self.driver.find_element(By.ID,'loginName').send_keys('admin')
        self.driver.find_element(By.ID,'password').send_keys('123456')
        time.sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input').submit()

    def do_search(self):
        # self.do_login()
        ele = self.driver.find_element(By.NAME,'keyWord')
        ele.send_keys('香')
        ele.send_keys(Keys.ENTER)




    def __del__(self):
        time.sleep(5)
        # self.driver.quit()

if __name__ == "__main__":
    u = YMW()
    u.do_login()
    u.do_search()

