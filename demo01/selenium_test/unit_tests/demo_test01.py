# coding=utf-8
from selenium.webdriver.common.by import By

from selenium import webdriver
import unittest
import time

class Test_baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        time.sleep(3)

    def test_case01(self):
        self.driver.find_element(By.ID,"kw").send_keys("aa")
        time.sleep(3)
        self.driver.find_element(By.ID,"su").click()
        time.sleep(3)

    @unittest.skip
    def test_case02(self):
        self.driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[1]').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        time.sleep(3)
