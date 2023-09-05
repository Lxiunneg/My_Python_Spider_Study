from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://taobao.com'
browser = webdriver.Chrome()
browser.get(url)
input = browser.find_element(by=By.ID, value='q')
input.send_keys('Huawei')
time.sleep(1)
input.clear()
input.send_keys('Logic')
button = browser.find_element(by=By.CLASS_NAME,value='btn-search')
button.click()