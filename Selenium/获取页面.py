from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=option)

url = 'https://spa2.scrape.center/'
browser.get(url)
input = browser.find_element(by=By.CLASS_NAME,value='logo-title')
print(input.id)
print(input.tag_name)
print(input.size)
