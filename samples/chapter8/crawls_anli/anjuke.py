from urllib import request, error
from lxml import etree
import json
import csv
import re
'''

'''
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
    # html = html.replace('\xa0', '')  #没用
    html = html.replace('&nbsp;', '--')   # 保存时有其他出编码错误的，也可以这样replace掉
    html = html.replace('\xb2', '')
    html = html.replace('\xa0', '')
    # 即使不保存，这个也要去掉，多余的字符串

    with open('anjuke.html', 'w') as f: # 第一次执行，保存为本地文件
        f.write(html)
    return html


def local_html():
    # 先用本地文件跑，等程序写完了，再从网站爬取
    with open('anjuke.html', 'r') as html:
        html = html.read()
    return html


def crawl_data(html):

    html = etree.HTML(html)
    html = etree.ElementTree(html)
    # 只要这部分html
    
    ul = etree.ElementTree(html.xpath('//ul[@id="houselist-mod-new"]')[0])
    print(ul)
    # 标题//*[@id="houselist-mod-new"]/li[2]/div[2]/div[1]/a
    titles = ul.xpath('/ul/li/div[2]/div[1]/a/@title')
    #print(titles)
    # 房型 //*[@id="houselist-mod-new"]/li[2]/div[2]/div[2]/span[1]
    roomstyle = ul.xpath('/ul/li/div[2]/div[2]/span[1]/text()')

    mianji = ul.xpath('/ul/li/div[2]/div[2]/span[2]/text()')
    cenggao = ul.xpath('/ul/li/div[2]/div[2]/span[3]/text()')
    niandai = ul.xpath('/ul/li/div[2]/div[2]/span[4]/text()')

    # price //*[@id="houselist-mod-new"]/li[3]/div[3]/span[1]/strong
    price = ul.xpath('/ul/li/div[3]/span[1]/strong/text()')


    # 地址 //*[@id="houselist-mod-new"]/li[2]/div[2]/div[3]/span
    address = ul.xpath('/ul/li/div[2]/div[3]/span/@title')
    
    rows = zip(titles, roomstyle, mianji, cenggao,niandai,price,address)

    #print(len(titles)==len(roomstyle)==len(mianji)==len(cenggao)==len(niandai)==len(price)==len(address))
    #print()



    return list(rows)

def save_to_json(data, filename):
    with open('{}.json'.format(filename), 'w') as json_file:
        json_file.write(json.dumps(data))

def save_to_csv(data, filename, mode='a'):
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


def read_from_json(filename):
    with open('{}.json'.format(filename), 'r') as json_file:
        data = json.load(json_file)
    return data


def _test():
    url = 'https://shanghai.anjuke.com/sale/p8/#filtersort'
    html = get_html(url)
    #html = local_html()  # 先用本地保存的html边调试边写代码
    data = crawl_data(html)
    save_to_csv(data, 'anjuke', mode='a')





if __name__ == '__main__':
    url = 'https://shanghai.anjuke.com/sale/p8/#filtersort'
    html = get_html(url)
    data = crawl_data(html)
    save_to_csv(data, 'anjuke', mode='a') 