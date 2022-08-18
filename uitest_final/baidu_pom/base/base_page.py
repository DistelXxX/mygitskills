from selenium import webdriver

class BasePage:
    #构建方法
    def __init__(self,driver):
        self.driver = driver

    #封装定位元素
    def find_ele(self,*args):
        return self.driver.find_element(*args)