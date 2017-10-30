from lxml import etree
html = '''
<bookstore>
    <book class="th">
        <title lang="en">Harry Potter</title>
        <price >29.99</price>
    </book>
    <book class="th vip" lang='cn'>
        <title lang="cn">Learning XML</title>
        <title>Learning Python</title>
        <price>39.95</price>
    </book>
</bookstore>
'''
html = etree.HTML(html)
html = etree.ElementTree(html)
#print(html)
#print(html.xpath('//bookstore/book[1]/title'))
#print(html.xpath('//bookstore/book/title[1]'))
print(html.xpath('//title[contains(text(), "Learning")]/text()'))