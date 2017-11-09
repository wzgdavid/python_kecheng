from urllib import request, error
from lxml import etree
import csv
import gevent
from gevent import monkey;monkey.patch_all()
import os
import requests
#url = 'http://china.huanqiu.com/article/2017-08/11138544.html?from=bdwz'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}
#response = request.urlopen(url) # 不带任何参数的请求
#print(response.status)
def get_html(url):
    '''得不到页面返回None'''
    html = None
    try:
        req = request.Request(url, headers=headers)
        response = request.urlopen(req)
        html = response.read().decode('gbk') # bytes
    except error.URLError as e:
        print('error.URLError')
        print(e, url)
    except error.HTTPError as e:
        print('error.HTTPError')
        print(e, url)
    except Exception as e:
        print(e, url)
    return html

def get_html2(url):
    r = requests.get(url, headers=headers)
    r.encoding = 'gbk'
    return r.text

url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

def crawl_data(html):
    html = etree.ElementTree(etree.HTML(html))
    items = html.xpath('//div[@id="resultList"]/div[@class="el"]')
    #print(len(items))
    rows = []
    for i, item in enumerate(items):
        print(i)
        #print(type(item))
        # 这个item就是class=“el”的div
        item = etree.ElementTree(item)
        #print(type(item))
        title = item.xpath('/div/p/span/a/@title')[0]
        link = item.xpath('/div/p/span/a/@href')[0]
        company = item.xpath('/div/span[1]/a/text()')[0]
        area = item.xpath('/div/span[2]/text()')
        area = area[0] if area else None
        salary = item.xpath('/div/span[3]/text()')
        #if salary: # salary不是空的时候
        #    salary = salary[0]
        #else:
        #    salary = None
        salary = salary[0] if salary else None
        #print(link)
        detail_page = get_html(link)#  得到详细页面
        if detail_page:
            detail_page = etree.ElementTree(etree.HTML(detail_page))
            #print(detail_page)
            exp = detail_page.xpath('//div[@class="jtag inbox"]/div/span/em[@class="i1"]/parent::span/text()')
            exp = exp[0] if exp else None
            xueli = detail_page.xpath('//div[@class="jtag inbox"]/div/span/em[@class="i2"]/parent::span/text()')
            xueli = xueli[0] if xueli else None
            #print(exp, xueli)
        # 一条记录
        row = title,company,area,salary,exp,xueli,link
        # 所有记录
        #print(row)
        rows.append(row)
    return rows

# 'w' 写 'r' 读  'a' 追加写入
def write_to_csv(filename, mode, rows):
    with open(filename, mode, newline='') as jobs:
        writer = csv.writer(jobs)
        if mode == 'w':
            writer.writerow(('职位名','公司','工作地点','薪资','经验','学历','url'))
        writer.writerows(rows)

## 两个写法等价
#def write_to_csv(filename, mode, rows):
#    # jobs 是一个打开的文件
#    jobs = open(filename, mode, newline='')
#    writer = csv.writer(jobs)
#    if mode == 'w':
#        writer.writerow(('职位名','公司','工作地点','薪资','经验','学历','url'))
#    writer.writerows(rows)
#    jobs.close()
def write_to_csv_auto(filename, rows):

    #path = os.getcwd() + '\\' + filename #
    path = ''.join([os.getcwd(), '\\', filename])
    #print(path)
    size = 0
    try:
        size = os.path.getsize(path)
    except FileNotFoundError as e:
        print(e)
    
    if size == 0:
        write_to_csv(filename, 'w', rows)
    else:
        write_to_csv(filename, 'a', rows)

def crawl_one_page(url):
    html = get_html2(url)
    rows = crawl_data(html)
    #print(rows)
    #write_to_csv('jobs.csv', 'a', rows)
    write_to_csv_auto('jobs2.csv', rows)

#tasks = []
#for n in range(1, 2):
#    url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(n)
#    task = gevent.spawn(crawl_one_page, url)
#    tasks.append(task)
#    # 生成一个任务列表
#    #crawl_one_page(url)
#gevent.joinall(tasks) # 并发运行

url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

crawl_one_page('http://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=')

#html = get_html2(url)
#print(html)