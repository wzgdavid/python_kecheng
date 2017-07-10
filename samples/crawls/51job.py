from urllib import request, error
from lxml import etree
import json
import csv

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
    except error.URLError as e:
        print(e)
    except error.HTTPError as e:
        print(e)
    html = response.read().decode('gbk')
    with open('sample.html', 'w') as f: # 第一次执行，保存为本地文件
        f.write(html)
    return html


def local_html():
    # 先用本地文件跑，等程序写完了，再从网站爬取
    with open('sample.html', 'r') as html:
        html = html.read()
    return html


def crawl_data(html):
    html = etree.HTML(html)
    html = etree.ElementTree(html)
    content = etree.ElementTree(html.xpath('//div[@id="resultList"]')[0])
    #titles = content.xpath('/div/div[@class="el"]/p/span/a/text()')
    #titles = [n.strip() for n in titles]
    #print(len(titles))
    #companies = content.xpath('/div/div[@class="el"]/span/a/text()')
    #companies = [n.strip() for n in companies]
    #print(len(companies))
    #places = content.xpath('/div/div[@class="el"]/span[@class="t3"]/text()')
    #places = [n.strip() for n in places]
    #print(len(places))
    #salaries = content.xpath('/div/div[@class="el"]/span[@class="t4"]/text()')
    #salaries = [n.strip() for n in salaries]
    #print(len(salaries))
    #times = content.xpath('/div/div[@class="el"]/span[@class="t5"]/text()')
    #times = [n.strip() for n in times]
    #print(len(times))
    
    results = []
    for n in range(1, 51):
        title = content.xpath('/div/div[@class="el"][{}]/p/span/a/text()'.format(n))[0].strip()
        company = content.xpath('/div/div[@class="el"][{}]/span/a/text()'.format(n))[0].strip()
        salary = content.xpath('/div/div[@class="el"][{}]/span[@class="t4"]/text()'.format(n))
        # salary 会有空
        if not salary:
            salary.append(None)
        salary = salary[0]
        place = content.xpath('/div/div[@class="el"][{}]/span[@class="t3"]/text()'.format(n))[0]
        publish_date = content.xpath('/div/div[@class="el"][{}]/span[@class="t5"]/text()'.format(n))[0]
        one = (title, company, place, salary, publish_date)
        results.append(one)
    print(results)
    return results


def save_to_csv(data, filename):
    for n in data:
        print(n)
    with open("{}.csv".format(filename), "a", newline="") as datacsv:
        writer = csv.writer(datacsv)
        # 写入标题
        #writer.writerow(["职位名","公司名","工作地点","薪资","发布时间"])
        writer.writerows(data)


def _test():
    url = 'http://search.51job.com/list/020000,000000,0000,00,9,99,%2520,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(1) # format里页数
    #html = get_html(url)

    html = local_html()  # 先用本地保存的html边调试边写代码
    data = crawl_data(html)
    save_to_csv(data, 'jobs')

if __name__ == '__main__':

    _test()