import urllib.request,http.cookiejar

#filename = 'MozillaTypeCookie.txt'
#cookie = http.cookiejar.MozillaCookieJar(filename)

filename = 'LWPTypeCookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)