from urllib.parse import urljoin
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import pymongo
import logging
# 设置日志输出格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'    # 列表页的URL构造
TIME_OUT = 10                                           # 延时
TOTAL_PAGE = 10                                         # 总页数

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'Selenium'
MONGO_COLLECTION_NAME = 'movies'

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# 将浏览器初始化为Chorme浏览器
browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, TIME_OUT)                  # 显示设置延时


def scrape_page(url, condition, locator):
    """_summary_
    爬取的通用函数

    Args:
        url (str): 待爬取的页面URL
        condition (bool): 页面加载成功的判断条件
                            一般是EC.visibility_of_all_elements_located。
                            EC.visibility_of_all_elements_located 是 Selenium 中的一个条件，用于等待页面上所有元素都可见。
                            或者是EC.visibility_of_elements_located
                            EC.visibility_of_elements_located 是 Selenium 中的一个条件，用于等待页面上至少一个元素可见。
        locator (tuple): 定位器，是一个元组，通过配置查询条件和参数来查找节点
    """

    logging.info('scraping %s', url)
    try:
        browser.get(url)  # 获取页面
        wait.until(condition(locator))  # 延时等待
    except TimeoutException:
        logging.error('error occured while scraping %s', url, exe_info=True)


def scrape_Index(page):
    """_summary_
    爬取详情页
    Args:
        page (int): 页面的秩
    """
    url = INDEX_URL.format(page=page)  # 构造详情页的URL
    scrape_page(url=url, condition=EC.visibility_of_all_elements_located,
                locator=(By.CSS_SELECTOR, '#index .item'))


def parse_index():
    """_summary_
    分割URL的加密参数
    Yields:
        str: 解析之后的URL
    """
    elements = browser.find_elements(
        by=By.CSS_SELECTOR, value='#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL, href)


def scrape_detail(url):
    """_summary_
    调用scrape_page()来爬取详情页的信息

    Args:
        url (str): 详情页的URL
    """
    # h2的节点是调用名称对应的节点
    scrape_page(url=url, condition=EC.visibility_of_all_elements_located,
                locator=(By.CSS_SELECTOR, 'h2'))


def parse_detail():
    """_summary_
    爬取详情页
    """
    url = browser.current_url
    name = browser.find_element(by=By.TAG_NAME, value='h2').text
    categories = [element.text for element in browser.find_elements(
        by=By.CSS_SELECTOR, value='.categories button span')]
    cover = browser.find_element(
        by=By.CSS_SELECTOR, value='.cover').get_attribute('src')
    score = browser.find_element(by=By.CLASS_NAME, value='score').text
    drama = browser.find_element(by=By.CSS_SELECTOR, value='.drama p').text

    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


def save_data(data):
    """_summary_
    将JSON数据存储到MongoDB
    Args:
        data (dict): 爬取的数据
    """
    collection.update_one({'name': data.get('name')},
                          {'$set': data}, upsert=True)

def main():
    """
    爬取的主函数
    """
    try:
        for page in range(1, TOTAL_PAGE+1):
            scrape_Index(page)
            detail_urls = parse_index()
            # logging.info('detail urls %s', list(detail_urls))
            for detail_url in list(detail_urls):
                logging.info('get detail url %s', detail_url)
                scrape_detail(detail_url)
                detail_data = parse_detail()
                save_data(detail_data)
                logging.info('detail data saved successful!')
    finally:
        browser.close()


if __name__ == '__main__':
    main()
    print('seccessful!')
