import unittest
from ddt import ddt,data
from selenium import webdriver

from baidu_pom.po.baidu_page import BaiduPage

@ddt
class BaiduTest(unittest.TestCase):

    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        #加载百度首页
        self.driver.get("https://www.baidu.com/")
        #窗口最大化
        self.driver.maximize_window()
    @data("软件测试","硬件测试")
    def test01(self,seaString):
        BaiduPage(self.driver).search(seaString)


if __name__ == '__main__':
    unittest.main()