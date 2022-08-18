# coding=utf-8
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from ymw_pom.base.BaseTools import Base_tools
class Ymw_oper(Base_tools):
    ymw_url = "http://localhost:8080/EasyBuy/Login?action=toLogin"
    username = (By.NAME,'loginName')
    password = (By.NAME,'password')
    btn = (By.CLASS_NAME,'log_btn')

    # 打开易买网
    def open(self):
        self.getUrl(self.ymw_url)
        time.sleep(3)

    # 登录易买网
    def doLogin(self,usr,passwd):
        self.inputData(self.username,usr)
        time.sleep(2)
        self.inputData(self.password,passwd)
        time.sleep(2)
        self.doClick(self.btn)
        time.sleep(1)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    ymw = Ymw_oper(driver)
    ymw.open()
    ymw.doLogin('admin','123456')