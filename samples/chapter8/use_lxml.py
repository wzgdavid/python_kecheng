from lxml import etree
from pprint import pprint
import json


html1 = '''
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title"><b> The Dormouse's story</b></p>
        <p class="story">
           Once upon a time there were three little sisters; and their names were
           <a class="sister" href="http://example.com/elsie" id="link1">
            Elsie
           </a>,
           <a class="sister" href="http://example.com/lacie" id="link2">
            Lacie
           </a>and
           <a class="sister" href="http://example.com/tillie" id="link2">
            Tillie
           </a>
           ; and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
    </body>
</html>
'''
html2 = '''
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
html = etree.fromstring(html2)

book_keys = ['title', 'title_lang', 'price']
#print(book_dict)
books = html.xpath("//book")
books_result = []
for i, book in enumerate(books):
    book_dict = dict.fromkeys(book_keys)
    book_dict['title'] = html.xpath('//book[{}]/title/text()'.format(i+1))[0]
    book_dict['title_lang'] = html.xpath('//book[{}]/title/@lang'.format(i+1))[0]
    book_dict['price'] = float(html.xpath('//book[{}]/price/text()'.format(i+1))[0])
    books_result.append(book_dict)

pprint(books_result)
print(json.dumps(books_result, sort_keys=True, indent=4))

with open('books.json', 'w') as json_file:
    json_file.write(json.dumps(books_result))
with open('books.json') as json_file:
    data = json.load(json_file)

pprint(data)
