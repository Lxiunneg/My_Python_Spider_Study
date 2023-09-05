from selenium import webdriver
import time
browser = webdriver.Chrome()

browser.get('https://www.baidu.com')
browser.get('https://www.zhihu.com')
browser.get('https://www.bilibili.com')

browser.back()
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()