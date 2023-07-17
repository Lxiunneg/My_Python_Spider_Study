import urllib.request, http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
cookie.load('LWPTypeCookie.txt',ignore_expires=True,ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))