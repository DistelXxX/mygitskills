# coding=utf-8
import json

from selenium.webdriver.common.by import By

from selenium import webdriver

from test02.mysqlconnect import UandP
import time
class QQemail():
    # def __init__(self):
    # # def opemail(self):
    #     self.driver = webdriver.Chrome()
    #
    #     time.sleep(2)
    def __init__(self,driver):
        self.driver = driver

    def baidu_search(self,keyword):
        # driver = self.baidu()
        self.driver.get("https://www.baidu.com")
        time.sleep(1)
        self.driver.find_element(By.ID,'kw').send_keys(keyword)
        self.driver.find_element(By.ID,'su').click()
        time.sleep(2)
    def email_login(self,username):
        u = UandP()
        b = u.getUsernameAndPassword(username)

        # 打开
        self.driver.find_element(By.XPATH,'//*[@id="1"]/div/div[1]/h3/a').click()
        time.sleep(1)


        all_handles = self.driver.window_handles

        self.driver.switch_to.window(all_handles[1])
        time.sleep(3)

        # 切换iframe
        self.driver.switch_to.frame(0)
        time.sleep(1)
        # 获取用户输入框
        self.driver.find_element(By.NAME,'email').send_keys(b[1])
        self.driver.find_element(By.NAME,'password').send_keys(b[2])
        time.sleep(3)
        self.driver.find_element(By.ID,'dologin').click()

        time.sleep(5)

    def save_cookies(self):
        mycookies = self.driver.get_cookies()
        jsoncookies = json.dumps(mycookies)
        with open("mycookies.json","w") as f:
            f.write(jsoncookies)

    def __del__(self):
        time.sleep(2)
        # self.driver.close()
        # self.driver.quit()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    u = QQemail(driver)
    u.baidu_search('网易邮箱')
    u.email_login('15970926681')
    u.save_cookies()

