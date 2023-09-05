from selenium import webdriver
from selenium.webdriver.common.by import By

# 导入selenium库中的By模块，用于指定元素定位方式
browser_Chrome = webdriver.Chrome()
# browser_Safari = webdriver.Safari()
# browser_Edge = webdriver.Edge()
# browser_Firefox = webdriver.Firefox()

browser_Chrome.get('https://www.taobao.com')
# print(browser_Chrome.page_source)

# input_1 = browser_Chrome.find_element(by=By.ID, value='q')
# input_2 = browser_Chrome.find_element(by=By.CSS_SELECTOR, value='#q')
# input_3 = browser_Chrome.find_element(by=By.XPATH, value='//*[@id="q"]')
# print(input_1, '\n', input_2, '\n', input_3)

input = browser_Chrome.find_elements(by=By.CSS_SELECTOR,value='.service-bd li')
print(input)

browser_Chrome.close()
