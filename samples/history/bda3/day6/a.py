#获取网页
#urllib库
#第三方库 requests  （conda list）（pip install requests）
#
#解析网页
#lxml   etree    
#etree.ElementTree
#Xpath
#其他 beautifulsoup
#获取到数据
#
#保存 （数据持久化）
#数据库
#csv （文件）


from urllib import request, error # 标准库
from lxml import etree   # 第三方
import csv  # 标准库

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Connection':'keep-alive',
}

def get_html(url, encoding='utf-8'):
    html = None # html变量可能会存在未定义的情况
    req = request.Request(url, headers=headers) # 构造一个请求对象
    try:
        response = request.urlopen(req)
        html_bytes = response.read()  # 读取响应中的字节流 bytes
        html = html_bytes.decode(encoding)  # 解码
    except error.URLError as e:
        print(e, url)
    except error.HTTPError as e:
        print(e, url)
    except Exception as e:
        print(e, url)

    return html

def get_data(html):
    html = etree.ElementTree(etree.HTML(html))
    items = html.xpath('//div[@id="resultList"]//div[@class="el"]')
    # //*[@id="resultList"]/div[4]
    #print(len(div_els))
    #print(items)
    rows = []
    for item in items:
        # 从每一个class是el 的 div中 查找
        item = etree.ElementTree(item)
        # //*[@id="resultList"]/div[4]/p/span/a/@title
        title = item.xpath('/div/p/span/a/@title')[0]
        #print(title)
        # //*[@id="resultList"]/div[5]/span[3]
        company = item.xpath('/div/span[1]/a/@title')[0]
        #print(company)
        place = item.xpath('/div/span[2]/text()')[0]
        #print(place)
        salary = item.xpath('/div/span[3]/text()')
        #if salary: # if salary != []  if len(salay) !=0
        #    salary = salary[0]
        #else:
        #    salary = None
        salary = salary[0] if salary else None # 条件表达式
        # //*[@id="resultList"]/div[5]/p/span/a
        link = item.xpath('/div/p/span/a/@href')[0]
        detail_page = get_html(link, 'gbk')
        if detail_page: # 有详细页才去解析（某些是停止招聘或过期职位）
            detail_page = etree.ElementTree(etree.HTML(detail_page))
            # /html/body/div[3]/div[2]/div[3]/div[1]/div/div/span[1]/em
            exp = detail_page.xpath('//div[@class="t1"]/span/em[@class="i1"]/parent::span/text()') #  
            exp = exp[0] if exp else None
            xueli = detail_page.xpath('//div[@class="t1"]/span/em[@class="i2"]/parent::span/text()') #  
            xueli = xueli[0] if xueli else None
            #print(exp,xueli)
        #break                                                                                                     
        row = title, company, place, salary, exp, xueli, link # 一条记录
        #print(row)
        rows.append(row)
    return rows

def save_to_csv(data, filename, mode):
    # f = open(filename, mode, newline='')
    with open(filename, mode, newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == '__main__':

    url = 'http://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    html = get_html(url, encoding='gbk')
    rows = get_data(html)
    save_to_csv(rows, '51python.csv', 'a')