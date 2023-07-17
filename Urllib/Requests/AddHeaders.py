import requests

headers = {
    'User-Agent':'Mozilla/5.0, Windows NT'
}

r = requests.get('https://ssr1.scrape.center/',headers=headers)
print(r.text)