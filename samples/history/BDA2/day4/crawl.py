from urllib import request, error

url = 'http://china.huanqiu.com/article/2017-08/11138544.html?from=bdwz'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}
#response = request.urlopen(url) # 不带任何参数的请求
#print(response.status)
def get_html(url):
    html = None
    try:
        req = request.Request(url, headers=headers)
        response = request.urlopen(req)
        html = response.read().decode('utf-8') # bytes
    except error.URLError as e:
        print('error.URLError')
        print(e, url)
    except error.HTTPError as e:
        print('error.HTTPError')
        print(e, url)
    except Exception as e:
        print(e, url)
    return html

#a ='你好'
#a1 = a.encode('utf-8')
#print(a1)
#print(a1.decode('gbk'))
html = get_html(url)
print(html)


<bookstore>
    <book>
        <title lang="en">Harry Potter</title>
        <price >29.99</price>
    </book>
    <book>
        <title lang="cn">Learning XML</title>
        <price>39.95</price>
    </book>
</bookstore>
