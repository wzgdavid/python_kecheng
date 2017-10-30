#encoding: utf-8
##import urllib
from lxml import etree
from pprint import pprint
#print(lxml)
from urllib import request, error
import csv
url = 'http://docs.jinkan.org/docs/jinja2/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
}

#response = request.urlopen(url)
#html = response.read().decode('utf-8')
#print()

# 假装成浏览器，用headers
req = request.Request(url, headers=headers)
try:
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    #print(html)
except error.URLError as e:
    print(e, url)
except error.HTTPError as e:
    print(e, url)
except Exception as e:
    print(e, url)


xml = '''
<bookstore>
    <book>
        <title lang="en">Harry Potter</title>
        <price>29.99</price>
    </book>
    <book>
        <title lang="cn">java</title>
        
    </book>
    <book>
        <title lang="cn">Learning XML</title>
        <price>39.95</price>
    </book>

</bookstore>
'''
#//*[@id="jinja2"]/h1
##html = 
html = etree.ElementTree(etree.HTML(xml))
#print(html)
books = html.xpath('//book')

all_books = []
for i, book in enumerate(books):
    # book是Element，转成ElementTree
    book_tree = etree.ElementTree(book)
    title = book_tree.xpath('/book/title/text()')[0]
    lang = book_tree.xpath('/book/title/@lang')[0]
    # []    就好比 if False:
    # ['en']

    price_list = book_tree.xpath('/book/price/text()')
    # if len(price_list) != 0:
    if price_list: # 判断列表, 非空时进入这个分支
        price = price_list[0]
    else:   # 列表为空
        price = None
    all_books.append((title, lang, price))

pprint(all_books)

# 'w' 写入，
# 'a'  追加写入
# 'r'  读
with open('books.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    #titles = ('书名', '语言', '价格')
    #writer.writerow(titles)
    writer.writerows(all_books)

