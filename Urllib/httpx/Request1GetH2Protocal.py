import requests

url = 'https://spa16.scrape.center/'

r = requests.get(url)
print(r.text)