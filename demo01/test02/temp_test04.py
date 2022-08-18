# coding=utf-8
from selenium import webdriver
import time

class Mylib():

    def __init__(self, brower):
        '''
            初始化浏览器对象
        '''
        # 根据传入的参数创建对应的浏览器对象，前提是所有的浏览器驱动都已经正确安装
        if brower == 'Firefox':
            self.driver = webdriver.Firefox()
        elif brower == 'Chrome':
            self.driver = webdriver.Chrome()
        elif brower == 'PhantomJS':
            self.driver = webdriver.PhantomJS()
        # 设置浏览器全屏
        self.driver.maximize_window()

    def delay(self):
        '''
            延迟等待
        '''
        self.driver.implicitly_wait(5)

    def open_url(self, url):
        '''
            访问网站
        '''
        self.driver.get(url)
        self.delay()
        print('访问:%s成功'%url)

    def __del__(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    web = Mylib('Chrome')
    web.open_url('http://www.baidu.com')
    web.open_url('http://www.renren.com')