from selenium.webdriver.common.by import By
from baidu_pom.base.base_page import BasePage
import time

#继承BasePage类
class BaiduPage(BasePage):
    #元素定位
    baidu_text_loc = (By.ID, "kw")
    baidu_submit_loc = (By.ID,"su")

    #获得元素对象
    def get_text_obj(self):
        return self.find_ele(*BaiduPage.baidu_text_loc)
    def get_submit_obj(self):
        return self.find_ele(*BaiduPage.baidu_submit_loc)
    #页面操作
    def search(self,search_string):
        self.get_text_obj().send_keys(search_string)
        self.get_submit_obj().click()

        time.sleep(5)

# u = BaiduPage()
# u.get_text_obj()