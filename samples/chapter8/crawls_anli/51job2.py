'''
这边抓取到的数据，用
chapter10的anli_51job.py
来机器学习并预测职位薪资
'''

from urllib import request, error
from lxml import etree
import json
import csv
import gevent
from gevent import monkey; monkey.patch_all()


headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
    "Referer": "http://search.51job.com/",
    'Connection': 'keep-alive'
}

def get_html(url):

    req = request.Request(url, headers=headers)
    try:
        #response = request.urlopen(url)
        response = request.urlopen(req)
        html = response.read().decode('gbk')
    except error.URLError as e:
        print(e)
        html = None
    except error.HTTPError as e:
        print(e)
        html = None
    
    #print(html)
    #with open('51jobs.html', 'w') as f: # 第一次执行，保存为本地文件
    #    f.write(html)
    return html


#def local_html():
#    # 先用本地文件跑，等程序写完了，再从网站爬取
#    with open('..\csv\51jobs.html', 'r') as html:
#        html = html.read()
#    return html

#def _get_salary(salary_str):
#
#    '''
#    0.8-1.2万/月   
#    4-6千/月
#    15-20万/年
#    100元/天
#    是爬数据时处理还是做机器学习时处理
#    '''

def crawl_data(html):
    html = etree.HTML(html)
    html = etree.ElementTree(html)

    items = html.xpath('//div[@id="resultList"]/div[@class="el"]')
    rows = []
    for i, item in enumerate(items):
        item = etree.ElementTree(item)
        #print(item, i)
        #title = item.xpath('//p[@class="t1 "]/span/a/@title')[0]
        #有些带图标的p的类名不是t1，是"t1 tg", 所以用contain
        title = item.xpath('//p[contains(@class,"t1")]/span/a/@title')[0]
        link = item.xpath('//p[contains(@class,"t1")]/span/a/@href')[0]
        company = item.xpath('//span[@class="t2"]/a/@title')[0]
        area = item.xpath('//span[@class="t3"]/text()')[0]
        salary = item.xpath('//span[@class="t4"]/text()')
        salary = salary[0] if salary else None
        #print(i, salary)
        # 经验和学历
        
        detail = get_html(link)
        if detail:
            detail = etree.ElementTree(etree.HTML(detail))
            exp = detail.xpath('//div[@class="jtag inbox"]//em[@class="i1"]/following::text()[1]')
            exp = exp[0] if exp else None
            xueli = detail.xpath('//div[@class="jtag inbox"]//em[@class="i2"]/following::text()[1]')
            xueli = xueli[0] if xueli else None
        else:
            continue
        print(i, exp, xueli)
        row = (title, link, company, area, salary, exp, xueli)
        rows.append(row)
    return rows


def save_to_csv(data, filename, mode):
    #for n in data:
    #    print(n)
    with open(filename, mode, newline="") as datacsv:
        writer = csv.writer(datacsv)
        # 写入标题
        if mode =='w':
            writer.writerow(["职位名","链接", "公司","工作地点","薪资","经验","学历"])
        else:
            pass
        writer.writerows(data)


def crawl_one(url):
    #url = 'http://search.51job.com/list/020000,000000,0000,00,9,99,%2520,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(1) # format里页数

    html = get_html(url)
    #html = local_html()  # 先用本地保存的html边调试边写代码
    if html:
        data = crawl_data(html)
        save_to_csv(data, r'51jobs.csv', mode='a')

def run():
    tasks = []
    url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    for n in range(22, 32):
        tasks.append(gevent.spawn(crawl_one, url.format(n)))
    gevent.joinall(tasks)

if __name__ == '__main__':
    #url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(1)
    #crawl_one(url)
    run()