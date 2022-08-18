# coding=utf-8

from selenium.webdriver.common.by import By

from selenium import webdriver
import unittest
import time

from selenium_test.unit_tests.qq_email import QQemail
from selenium_test.unit_tests.yimaiwang import YMW


class Test_QQ_email(unittest.TestCase):
    # def setUp(self):
    #     self.driver=webdriver.Chrome()
    #     self.driver.get("https://www.baidu.com")
    #     self.driver.maximize_window()
    #     time.sleep(3)
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.u = QQemail(self.driver)
        self.a = YMW(self.driver)

    def test_case01(self):
        self.u.baidu_search('网易邮箱')
        self.u.email_login('15970926681')
        time.sleep(1)

    def test_case02(self):
        self.a.do_login()
        self.a.do_search()
        time.sleep(1)
    # @unittest.skip
    # def test_case02(self):
    #     self.driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[1]').click()
    #     time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()