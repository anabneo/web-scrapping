from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError

url = 'https://www.alura.com.br/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    print(html)

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)
