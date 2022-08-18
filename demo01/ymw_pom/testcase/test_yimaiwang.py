# coding=utf-8
import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from ymw_pom.po.ymw_operations import Ymw_oper

class Test_ymw(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        time.sleep(3)

    def test_case01(self):
        ymw = Ymw_oper(self.driver)
        ymw.open()
        ymw.doLogin('admin','123456')

if __name__ == '__main__':
    unittest.main()