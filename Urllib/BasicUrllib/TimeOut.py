import urllib.request
import socket
import urllib.error

try:
    response = urllib.request.urlopen('https://www.baidi.com', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
