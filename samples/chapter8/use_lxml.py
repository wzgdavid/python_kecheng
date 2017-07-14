from lxml import etree
from pprint import pprint
import json


html = '''
<bookstore>
  <book>
    <title lang="en">Harry Potter</title>
    <price>29.99</price>
  </book>
  <book>
    <title lang="cn">Learning XML</title>
    <price>39.95</price>
  </book>
  <book>
    <title lang="cn">One Piece</title>
    <price>135.50</price>
  </book>
</bookstore>
'''
#html = etree.fromstring(html)
html = etree.HTML(html)     
html = etree.ElementTree(html)    


# 一条记录做成字典
#book_keys = ['title', 'title_lang', 'price']
##print(book_dict)
#books = html.xpath("//book")
#allbook = []
#for i, book in enumerate(books):
#    book_dict = dict.fromkeys(book_keys)
#    book_dict['title'] = html.xpath('//book[{}]/title/text()'.format(i+1))[0]
#    book_dict['title_lang'] = html.xpath('//book[{}]/title/@lang'.format(i+1))[0]
#    book_dict['price'] = float(html.xpath('//book[{}]/price/text()'.format(i+1))[0])
#    allbook.append(book_dict)
#
#pprint(allbook)
#print(json.dumps(allbook, sort_keys=True, indent=4))

# 一条记录做成元组
books = html.xpath("//book")
allbook = []
for i, book in enumerate(books):
    title = html.xpath('//book[{}]/title/text()'.format(i+1))[0]
    lang = html.xpath('//book[{}]/title/@lang'.format(i+1))[0]
    price = float(html.xpath('//book[{}]/price/text()'.format(i+1))[0])
    onebook = (title, lang, price)
    allbook.append(onebook)
pprint(allbook)
#print(json.dumps(allbook, sort_keys=True, indent=4))

#with open('books.json', 'w') as json_file:
#    json_file.write(json.dumps(allbook))
#with open('books.json') as json_file:
#    data = json.load(json_file)
#
#pprint(data)
