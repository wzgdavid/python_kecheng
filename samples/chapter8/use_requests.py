import requests
from lxml import etree

#r = requests.get('https://github.com/timeline.json')
#print( type(r.json()) )


url = 'http://s.weibo.com/weibo/%25E9%25A9%25AC%25E8%258B%258F%25E5%25B7%25A5%25E4%25BD%259C%25E5%25AE%25A4%25E5%25A3%25B0%25E6%2598%258E&page=3'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
}
r = requests.get(url,headers=headers)

html = r.content.decode('utf-8')



# 然后用lxml
html = etree.HTML(html)
html = etree.ElementTree(html)



btn = html.xpath('//*[@id="pl_weibo_direct"]/div/div[2]/div/div[1]/div/div[1]/dl/div/div[3]/div[1]/a[1]')
print(btn)


