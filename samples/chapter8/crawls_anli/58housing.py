from urllib import request, error
from lxml import etree
import json
import csv
import re
'''

'''
def get_html(url):

    try:
        response = request.urlopen(url)
        #response = request.urlopen(req)
    except error.URLError as e:
        print(e)
    except error.HTTPError as e:
        print(e)
    html = response.read().decode('utf-8')
    # html = html.replace('\xa0', '')  #没用
    html = html.replace('&nbsp;', '')   # 有其他出编码错误的，也可以这样replace掉

    with open('58housing.html', 'w') as f: # 第一次执行，保存为本地文件
        f.write(html)
    return html


def local_html():
    # 先用本地文件跑，等程序写完了，再从网站爬取
    with open('58housing.html', 'r') as html:
        html = html.read()
    return html


def crawl_data(html):
    #html = etree.fromstring(html) # 这是个简单粗暴的方法，容易出错
    html = etree.HTML(html)
    html = etree.ElementTree(html)
    # 只要这部分html
    
    content = etree.ElementTree(html.xpath('//div[@class="mainbox"]//div[@class="main"]')[0])
    # 标题
    titles = content.xpath('/div/div/div/ul/li/div/h2/a[@onclick]/text()') 
    # 房型
    
    roomtype = content.xpath('/div/div/div/ul/li/div/p[@class="room"]/text()')
    
    # 房租
    rent = content.xpath('/div/div/div/ul/li/div[@class="listliright"]/div/b/text()')

    # 房租单位 比如元/月
    rent_unit = content.xpath('/div/div/div/ul/li/div[@class="listliright"]/div[@class="money"]/text()')
    
    # 地址
    address = content.xpath('/div/div/div/ul/li/div/p[@class="add"]/text()')
    #titles = [n.replace('\xa0', '').strip() for n in titles if n.strip()]  # 在整个网页把&nbsp;replace掉，就不用这三行了
    #roomtype = [n.replace('\xa0', '').strip() for n in roomtype if n.strip()]
    #rent_unit = [n.replace('\xa0', '').strip() for n in rent_unit if n.strip()]
    titles = [n.strip() for n in titles if n.strip()]
    roomtype = [n.strip() for n in roomtype if n.strip()]
    rent_unit = [n.strip() for n in rent_unit if n.strip()]
    #address = [n.strip() for n in address if n.strip()]

    #print(len(address), address)
    #rent_unit_striped = [n.strip() for n in rent_unit if n.strip()]

    #print(rent_unit_striped,2222)
    #print(len(titles))   # 打印长度看看是否匹配
    #print(len(authors))
    #print(len(last_reply))

    # 打印数据
    data = zip(titles, roomtype, rent, rent_unit)
    #print(data)
    d = list(data)
    print(len(d))

    return d

def save_to_json(data, filename):
    with open('{}.json'.format(filename), 'w') as json_file:
        json_file.write(json.dumps(data))

def save_to_csv(data, filename):
    for n in data:
        print(n)
    with open("{}.csv".format(filename), "a", newline="") as datacsv:
        writer = csv.writer(datacsv)
        # 写入标题
        writer.writerow(["标题","房型","房租","房租单位","地址"])
        #for row in data:
        #    writer.writerow(row)
        #data=[(1,2,3,4,5), (3,4,5,6,7)]
        writer.writerows(data)


def read_from_json(filename):
    with open('{}.json'.format(filename), 'r') as json_file:
        data = json.load(json_file)
    return data



def _test():
    url = 'http://sh.58.com/chuzu/pn50/'
    #url = 'http://sh.58.com/ershoufang/?PGTID=0d200001-0000-229e-4b38-eab0423532c9&ClickID=1'
    #url = 'http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=29150'
    html = get_html(url)
    #html = local_html()  # 先用本地保存的html边调试边写代码
    data = crawl_data(html)
    save_to_csv(data, '58housing')

    #data = read_from_json('tieba')
    #print(data)

if __name__ == '__main__':

    _test()