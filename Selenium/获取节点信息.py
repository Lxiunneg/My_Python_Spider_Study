from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=option)

url = 'https://spa2.scrape.center/'
browser.get(url)
logo = browser.find_element(by=By.CLASS_NAME, value='logo-image')
print(logo)
print(logo.get_attribute('src'))