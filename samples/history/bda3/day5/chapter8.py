from urllib import request, error, parse
from lxml import etree
#url = 'https://tieba.baidu.com/index.html'
url = 'https://tieba.baidu.com/p/5376439298'
url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=选择城市&kw=python&sm=0&p=1'
url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl='+parse.quote("选择城市")+'&kw=python&sm=0&p=1'
url = 'http://www.qq.com/'
#url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
#from urllib import request, error, parse
##url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&keyword=工程师&keywordtype=2'
#url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&keyword={}&keywordtype=2'.format(parse.quote("工程师"))
#print(url) # print结果 http://search.51job.com/jobsearch/search_result.php?fromJs=1&keyword=%E5%B7%A5%E7%A8%8B%E5%B8%88&keywordtype=2
response = request.urlopen(url) # 打开url获取内容
html = response.read() # bytes
#print(html)
print(html)
#html = html.decode('gbk')
#print(html)0=0==0============================================================================================================================================================================0=0==0==00==0==0==0==0===0=0===0==0==0=0=0=0=0==0=00=0=0=0==0==0==0=00==0===00=00==0=00=00=00=00=000=0=0=0=0==00=0=0=00==0=00=0=0==0=0=00=000=0=000=0=0=00=00=0000=00=0000=00=00=00=0=000=000=000=00=0=000=0=00=00=000=00=00=0=000=00=0=0=0=00=0=00=00=0000000=0==0=0=0=0=0=0========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================00=0000000000000000000000000000000000000000000000000=========0=00==0=00=0===0=0===0=0==00===0===0==0=00==0=0==0=0==00===00=0=0===00=00=0=00==0=0===0=0==0=00=0=0==0=0=0=00===00=0=0==00=000=0=00=0=0=0==00=0=0=0=000=0000=0=00=0==0=00=0================================================================================================================================================================================================================================================================

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Connection':'keep-alive',
}
# 构造一个请求

#req = request.Request(url, headers=headers)
##html = request.urlopen(req).read().decode('utf-8')
#try:
#    html = request.urlopen(req).read().decode('utf-8')
#except error.URLError as e:
#    print(e, url)
#except error.HTTPError as e:
#    print(e, url)
#except Exception as e:
#    print(e, url)
#

xml = '''
<bookstore>
    <title lang="en">TOm jerry</title>
    <book class='asdb'>
        <title lang="en" id='hp'>
            <price>666</price>Harry Potter
        </title>
        <price id='hpprice'>29.99</price>
    </book>
    <book>
        <title lang="cn" id='xml'>
            Learning XML
            <price id='xmlprice'>555</price>
        </title>
        <price>39.95</price>
    </book>
    <book>
        <title lang="cn">Learning python</title>
        <price>395.95</price>
    </book>
</bookstore>
'''
#<html>
#   <head></head>
#   <body></body>
#</html>
xml = etree.ElementTree(etree.HTML(xml))
#print(xml)

#print(xml.xpath('//bookstore/book')) # 节点
#print(xml.xpath('//bookstore/book/title/@id')) # 属性
#print(xml.xpath('//bookstore/title//text()')) # 文本
#print(xml.xpath('//bookstore/book[2]/title/price/text()')) # 555
## book下的第二个title，没有返回空
#print(xml.xpath('//bookstore/book/title[2]/price/text()')) # 
#print(xml.xpath('//bookstore/book[1]/title[1]/price/text()')) # 666
#print(xml.xpath('//bookstore//price[@id]')) # 有id的price元素
## 选择指定属性的元素
#print(xml.xpath('//bookstore//price[@id="hpprice"]/@id')) 
#print(xml.xpath('//bookstore//price[starts-with(@id, "hp")]/@id'))
#print(xml.xpath('//bookstore//price[contains(@id, "hp")]/@id')) 
#print(xml.xpath('//bookstore/*')) # bookstore下所有子节点
#print(xml.xpath('//bookstore/*[@*]')) # 
#<div class='abc'>
#<div class=' abc'>
#<div class='abc '>