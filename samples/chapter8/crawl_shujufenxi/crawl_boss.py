'''
从boss直聘抓取title包含'数据分析'的职位信息
'''

from urllib import request, error
from lxml import etree
import json
import csv
import time
import gevent

from gevent import monkey; monkey.patch_all()


headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
    "Referer": "http://search.51job.com/",
    'Connection': 'keep-alive'
}


def use_proxy(url):
    proxy_handler = request.ProxyHandler({'http': '122.96.59.103:82/'})
    proxy_auth_handler = request.ProxyBasicAuthHandler()
    #proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = request.build_opener(proxy_handler, proxy_auth_handler)
    response = opener.open(url)
    return response

def get_html(url):
    html = None
    try:
        req = request.Request(url, headers=headers)
        response = request.urlopen(req)
        #response = use_proxy(url)
        html = response.read().decode('utf-8')
    except error.URLError as e:
        print(e)
        print(url)
    except error.HTTPError as e:
        print(e)
        print(url)
    return html


def crawl_data(html):
    html = etree.HTML(html)
    html = etree.ElementTree(html)
    #//*[@id="main"]/div[3]/div[2]/ul/li[1]
    # items 一页所有记录, 15条
    items = html.xpath('//*[@id="main"]/div[3]/div[2]/ul/li')
    rows = []
    for i, item in enumerate(items):
        item = etree.ElementTree(item)
        #print(i)

        title = item.xpath('/li/a/div[1]/div[1]/h3/text()')[0]
        link = 'https://www.zhipin.com' + item.xpath('/li/a/@href')[0]
        company = item.xpath('/li/a/div[1]/div[2]/div/h3/text()')[0]
        area = item.xpath('/li/a/div[1]/div[1]/p/text()[1]')[0]
        salary = item.xpath('/li/a/div[1]/div[1]/h3/span/text()')
        salary = salary[0] if salary else None
        #print(i, salary)
        exp = item.xpath('/li/a/div[1]/div[1]/p/text()[2]')[0]
        xueli = item.xpath('/li/a/div[1]/div[1]/p/text()[3]')[0]
        row = (title, link, company, area, salary, exp, xueli)
        #print(row)
        rows.append(row)
    return rows


def save_to_csv(data, filename, mode):
    with open(filename, mode, newline="") as datacsv:
        writer = csv.writer(datacsv)
        # 写入标题
        if mode =='w':
            writer.writerow(["职位名","链接", "公司","工作地点","薪资","经验","学历"])
        # 写数据
        writer.writerows(data)


def crawl_one(url):
    html = get_html(url)
    if html:
        data = crawl_data(html)
        save_to_csv(data, r'boss.csv', mode='a')

def run():
    tasks = []
    url = 'https://www.zhipin.com/c100010000/h_100010000/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&page={}'
    for n in range(51, 300):
        print(n)
        crawl_one(url.format(n))
        time.sleep(2)

if __name__ == '__main__':
    #url = 'https://www.zhipin.com/c100010000/h_100010000/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&page=1'
    #crawl_one(url)
    run()