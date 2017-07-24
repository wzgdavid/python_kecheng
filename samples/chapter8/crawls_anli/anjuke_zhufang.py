from urllib import request, error
from lxml import etree
import json
import csv
import re
import time


def get_html(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
        "Referer": "https://shanghai.anjuke.com/",
        'Connection': 'keep-alive'
    }
    req = request.Request(url, headers=headers)
    try:
        #response = request.urlopen(url)
        response = request.urlopen(req)
    except error.URLError as e:
        print(e)
    except error.HTTPError as e:
        print(e)
    html = response.read().decode('utf-8')
    html = html.replace('\xa0', '')  #'\xa0'就是&nbsp;
    html = html.replace('&nbsp;', '')   # 保存时有其他出编码错误的，也可以这样replace掉
    html = html.replace('\xb2', '')
    
    return html


def crawl_data(html):

    html = etree.HTML(html)
    html = etree.ElementTree(html)

    #items = html.xpath('//div[@id="list-content"]/div[@class="zu-itemmod"]') # 为什么这个不行
    items = html.xpath('//div[@id="list-content"]/div[@_soj]')
    #print(items)
    for i, item in enumerate(items):
        #time.sleep(3)
        item = etree.ElementTree(item)
        title = item.xpath('//div[@class="zu-info"]/h3/a/@title')
        link = item.xpath('//div[@class="zu-info"]/h3/a/@href')
        print(i, link)
        detail = get_html(link)
        detail = etree.ElementTree(etree.HTML(detail))
        
    
    #rows = zip(titles, roomstyle, mianji, cenggao,niandai,price,address)


    return list(rows)


def save_to_csv(data, filename, mode='w'):
    for n in data:
        print(n)
    with open("{}.csv".format(filename), mode, newline="") as datacsv:
    #with open("{}.csv".format(filename), "a", newline="") as datacsv: # a是追加写入
        writer = csv.writer(datacsv)
        # 写入标题
        # zip(titles, roomstyle, mianji, cenggao,niandai,price,address)
        if mode=='w':
            writer.writerow(["标题","房型","面积","层高","年代","价格","地址"]) 
        else:
            pass
        writer.writerows(data)


def _test():
    url = 'https://sh.zu.anjuke.com/?from=navigation'
    html = get_html(url)
    data = crawl_data(html)
    save_to_csv(data, 'anjuke', mode='w')


if __name__ == '__main__':
    _test()
