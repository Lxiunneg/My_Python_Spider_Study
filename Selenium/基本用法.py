from selenium import webdriver
# 导入selenium库中的webdriver模块，用于驱动浏览器进行自动化操作

from selenium.webdriver.common.by import By
# 导入selenium库中的By模块，用于指定元素定位方式

from selenium.webdriver.common.keys import Keys
# 导入selenium库中的Keys模块，用于模拟键盘操作

from selenium.webdriver.support import expected_conditions as EC
# 导入selenium库中的EC模块，用于等待条件

from selenium.webdriver.support.wait import WebDriverWait
# 导入selenium库中的WebDriverWait模块，用于等待页面元素加载

browser = webdriver.Chrome()
# 创建一个Chrome浏览器的实例，用于自动化操作

try:
    browser.get('https://baidu.com')
    # 使用浏览器打开网页https://baidu.com

    # browser.find_element_by('kw') 方法已更新为以下方式
    input = browser.find_element(By.ID, 'kw')
    # 使用By.ID定位方式，找到id为'kw'的输入框元素，并将其赋值给input变量

    input.send_keys('Python')
    # 在输入框中输入关键字'Python'

    input.send_keys(Keys.ENTER)
    # 模拟键盘按下Enter键，提交搜索

    wait = WebDriverWait(browser, 10)
    # 设置一个最长等待时间为10秒的WebDriverWait对象，用于等待页面元素出现

    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    # 等待直到'id'为'content_left'的元素出现在页面中，即等待搜索结果加载完毕

    print(browser.current_url)
    # 打印当前页面的URL

    print(browser.get_cookies())
    # 打印当前页面的所有cookie信息

    print(browser.page_source)
    # 打印当前页面的源代码

finally:
    browser.close()
    # 关闭浏览器窗口