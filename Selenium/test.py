from selenium import webdriver
 

driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
 
 
# 登录百度
def main():
    driver.get("https://baidu.com/")
 
 
if __name__ == '__main__':
    main()