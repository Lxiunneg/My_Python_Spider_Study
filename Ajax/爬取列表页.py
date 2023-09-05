import requests
import logging
import pymongo

"""日志配置"""

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s')

"""MongoDB数据库配置"""

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME = 'movies'

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

"""URL的配置"""

INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
LIMIT = 10
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
TOTAL_PAGE = 10

"""爬取页面的接口"""


def scrape_api(url):
    logging.info('scrape %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


"""构造多个页面的url"""


def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=(page - 1) * LIMIT)
    return scrape_api(url)


"""详情页的爬取"""


def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)


"""数据保存到数据库"""


def save_data(data):
    collection.update_one({'name': data.get('name')}, {'$set': data}, upsert=True)

"""改写__main__"""

def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)
            save_data(detail_data)
            logging.info('data saved successfully!')


if __name__ == '__main__':
    main()
