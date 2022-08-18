"""
函数
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    chrome = webdriver.Chrome()
    chrome.get("https://www.baidu.com/")
    inputs = chrome.find_element(by=By.ID,value='kw')
    inputs.send_keys("中国人")

    sub = chrome.find_element(by=By.ID,value='su')
    sub.click()
    # chrome.quit()

