# coding=utf-8

class Base_tools:
    def __init__(self,driver):
        self.driver = driver

    # 获取网址
    def getUrl(self,url):
        return self.driver.get(url)

    # 获取元素对象
    def getEle(self,loc):
        return self.driver.find_element(*loc)

    # 输入数据
    def inputData(self,loc,txt):
        return self.getEle(loc).send_keys(txt)

    # 点击
    def doClick(self,loc):
        return self.getEle(loc).click()

if __name__ == '__main__':
    bt = Base_tools()

