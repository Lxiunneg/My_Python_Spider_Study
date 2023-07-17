import requests
from pyquery import PyQuery as pq
import re

url = 'https://ssr1.scrape.center/'
html = requests.get(url).text
doc = pq(html)
items = doc('.el-card').items()

# file = open('movies_TXT.txt','w',encoding='utf-8')
for item in items:
    #电影名称
    name = item.find('a > h2').text()
    #file.write(f'名称：{name}\n')
    # 类别
    categories = [item.text() for item in item.find('.categories button span').items()]
    #file.write(f'类别：{categories}\n')
    # 上映时间
    published_at_text = item.find('.info:contains(上映)').text()
    published_at = re.search('(\d{4}-\d{2}-\d{2})',published_at_text).group(1) \
        if published_at_text and re.search('(\d{4}-\d{2}-\d{2})',published_at_text) else None
    #file.write(f'上映时间：{published_at}\n')
    # 评分
    sorce =  item.find('p.score').text()
    #file.write(f'评分：{sorce}\n')
    #file.write(f'{"=" * 50}\n')
    with open('movies_TXT.txt','a',encoding='utf-8',) as file:
        file.write(f'名称：{name}\n')
        file.write(f'类别：{categories}\n')
        file.write(f'上映时间：{published_at}\n')
        file.write(f'评分：{sorce}\n')
        file.write(f'{"=" * 50}\n')