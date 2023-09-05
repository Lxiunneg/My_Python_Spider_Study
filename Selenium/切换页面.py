import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'

browser = webdriver.Chrome(options=option)
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element(by=By.CLASS_NAME, value='logo')
except NoSuchElementException:
    print('No Logo')
browser.switch_to.parent_frame()
logo = browser.find_element(by=By.CLASS_NAME, value='logo')
print(logo)
print(logo.text)
