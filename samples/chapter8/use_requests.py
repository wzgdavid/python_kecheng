import requests
from lxml import etree

#r = requests.get('https://github.com/timeline.json')
#print( type(r.json()) )


url = 'http://news.baidu.com/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
}
r = requests.get(url,headers=headers)

html = r.content.decode('utf-8')



# 然后用lxml
html = etree.HTML(html)
html = etree.ElementTree(html)


btn = html.xpath('//*[@id="sugarea"]/span[2]/input/@value')
print(btn)