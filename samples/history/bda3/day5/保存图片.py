from urllib import request, error#, urlretrieve
from lxml import etree
import csv
import urllib

def get_html(url, encoding='utf-8'):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Connection':'keep-alive',
    }
    # 构造一个请求
    req = request.Request(url, headers=headers)
    #html = request.urlopen(req).read().decode('utf-8')
    try:
        html = request.urlopen(req).read().decode(encoding)
    except error.URLError as e:
        print(e, url)
    except error.HTTPError as e:
        print(e, url)
    except Exception as e:
        print(e, url)

    return html

#a = open('temp1.csv', 'w') # a 代表一个文件
#csvwriter = csv.writer(a)
#csvwriter.writerow(tab_names)
#a.close()

#              'w'写入，覆盖  'a'追加内容  'r' read
#with open('temp2.csv', 'a', newline='') as a:
#    csvwriter = csv.writer(a)
#    csvwriter.writerow(tab_names)
# 可以写成函数
# 把data写入filename这个文件，
def write_to_csv(filename, mode, data):
    with open(filename, mode, newline='') as a:
        csvwriter = csv.writer(a)
        csvwriter.writerow(data)


 
# //*[@id="hdr"]/div/a
url = 'https://tieba.baidu.com/index.html'
html = get_html(url)
html = etree.ElementTree(etree.HTML(html))



# //*[@id="day_rcmd"]/div[1]/div/a/img
src = html.xpath('//*[@id="day_rcmd"]/div[1]/div/a/img/@src')[0]
request.urlretrieve(src, src.split('/')[-1]) 
#                   资源url, 本地文件名
#a = html.xpath('//div[@id="hdr"]/div/a/text()')
#print(a[0])
#
## //div[@id="nav"]/div/div/ul/li/a
#tab_names = html.xpath('//div[@id="nav"]/div/div/ul/li/a/text()')
#print(tab_names)
#lst = []
#write_to_csv('ttt.csv', data=tab_names, mode='a')
#write_to_csv('ttt.csv', data=lst, mode='a')