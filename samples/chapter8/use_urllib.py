from urllib import request, error

#url = 'https://docs.pyfffthon.org'
#try:
#    response = request.urlopen(url)
#except error.URLError as e:
#    print(e)
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/',
    'Connection': 'keep-alive'
}


url = 'http://blog.csdfdfdn.net/cqcresdfsd'
try:
    response = request.urlopen(url)
except error.URLError as e:
    print(e)
except error.HTTPError as e:
    print(e)

#print(response)