from selenium import webdriver
# 导入selenium库中的webdriver模块，用于驱动浏览器进行自动化操作

from selenium.webdriver.common.by import By
# 导入selenium库中的By模块，用于指定元素定位方式

from selenium.webdriver import ActionChains
# 导入selenium库中的ActionChains模块，用于模拟鼠标操作

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
# 创建ChromeOptions对象，用于设置浏览器选项
# add_experimental_option方法可以用于设置实验性选项，这里设置"detach"为True，表示不自动关闭浏览器窗口

browser = webdriver.Chrome(options=option)
# 创建一个Chrome浏览器的实例，并使用设置的选项进行配置

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# 设置目标网页的URL，这里是一个菜鸟网站的拖拽示例页面

browser.get(url)
# 使用浏览器打开指定的URL页面

browser.switch_to.frame('iframeResult')
# 切换到名为'iframeResult'的网页框架中，因为拖拽元素在该框架内

source = browser.find_element(by=By.CSS_SELECTOR, value='#draggable')
# 通过CSS选择器定位拖拽元素，返回一个WebElement对象，并将其赋值给source变量

target = browser.find_element(by=By.CSS_SELECTOR, value='#droppable')
# 通过CSS选择器定位目标元素，返回一个WebElement对象，并将其赋值给target变量

actions = ActionChains(browser)
# 创建ActionChains对象，用于模拟鼠标操作

actions.drag_and_drop(source, target)
# 使用drag_and_drop方法模拟鼠标拖拽操作，将source元素拖拽到target元素上

actions.perform()
# 执行ActionChains中的操作
d'f