from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 隐式等待
def implicitly_wait():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('https://spa2.scrape.center/')
    input = browser.find_element(by=By.CLASS_NAME, value='logo-image')
    print(input)


# 显示等待
def wait():
    browser = webdriver.Chrome()
    browser.get('https://taobao.com/')
    wait = WebDriverWait(browser, 10)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input,button)


if __name__ == '__main__':
    wait()
