import csv
from lxml import etree
from pprint import pprint
from urllib import request, error
import gevent
from gevent import monkey; monkey.patch_all()

url = 'http://docs.jinkan.org/docs/jinja2/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
}

def get_html(url):
    '''
    用urllib获取网页
    url 参数
    '''
    html = None
    req = request.Request(url, headers=headers)
    try:
        response = request.urlopen(req)
        html = response.read().decode('gbk')
    except error.URLError as e:
        print(e, url)
    except error.HTTPError as e:
        print(e, url)
    except Exception as e:
        print(e, url)
    return html


def crawl_data(html):
    '''
    从得到的网页中抓取数据
    '''
    # //div[@id="resultList"]/div[@class="el"]
    html = etree.ElementTree(etree.HTML(html))
    div_el = html.xpath('//div[@id="resultList"]/div[@class="el"]')
    #print(len(div_el))
    
    rows = [] # 放获取的所有职位信息
    for i, row in enumerate(div_el):
        print(i)
        row = etree.ElementTree(row)
        jobname = row.xpath('/div/p/span/a/@title')[0]
        link = row.xpath('/div/p/span/a/@href')[0]
        company = row.xpath('/div/span[@class="t2"]/a/@title')[0]
        area = row.xpath('/div/span[@class="t3"]/text()')
        area = area[0] if area else None
        salary = row.xpath('/div/span[@class="t4"]/text()')
        salary = salary[0] if salary else None
        # 获取详细页数据
        detail = get_html(link)
        if detail:
            detail = etree.ElementTree(etree.HTML(detail))
            #exp = detail.xpath('//div[@class="t1"]/span/em[@class="i1"]/following::text()')
            exp = detail.xpath('//div[@class="t1"]/span/em[@class="i1"]/parent::span/text()')
            xueli = detail.xpath('//div[@class="t1"]/span/em[@class="i2"]/parent::span/text()')
            exp = exp[0] if exp else None
            xueli = xueli[0] if xueli else None
            row = (jobname, link, company, area, salary,exp,xueli)
            rows.append(row)
    return rows

def save_to_csv(filename, data, mode='a'):
    with open(filename, mode, newline='') as file:
        writer = csv.writer(file)
        if mode == 'w':
            titles = ('职位名', '链接', '公司名', '工作地点', '薪资','经验','学历')
            writer.writerow(titles)
        writer.writerows(data)
  

url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,7.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
#html = get_html(url)
#data = crawl_data(html)
#save_to_csv(r'51job.csv', data, 'w')

def crawl_one_search(url):
    '''抓取一个搜索页'''
    html = get_html(url)
    data = crawl_data(html)
    save_to_csv(r'51job.csv', data)

for n in range(1,2):
    url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(n)
    crawl_one_search(url)

#tasks = []
#for n in range(4, 15):
#    url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(n)
#    tasks.append(gevent.spawn(crawl_one_search, url))
##print(tasks)
#gevent.joinall(tasks)