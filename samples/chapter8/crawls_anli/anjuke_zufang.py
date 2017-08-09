'''
这里抓取的数据用chapter10 anjuke_zufang.py 做推荐系统
'''

from urllib import request, error
from lxml import etree
import csv
import gevent
from gevent import monkey; monkey.patch_all()

def get_html(url):
    html = None
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
        "Referer": "https://shanghai.anjuke.com/",
        'Connection': 'keep-alive'
    }
    req = request.Request(url, headers=headers)
    try:
        #response = request.urlopen(url)
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
    except error.URLError as e:
        print(e)
        print(url)
    except error.HTTPError as e:
        print(e)
        print(url)
    
    #if html:
    #    html = html.replace('\xa0', '')  #'\xa0'就是&nbsp;
    #    html = html.replace('&nbsp;', '')   # 保存时有其他出编码错误的，也可以这样replace掉
    #    html = html.replace('\xb2', '')
    
    return html


def crawl_data(html):

    html = etree.HTML(html)
    html = etree.ElementTree(html)

    items = html.xpath('//div[@id="list-content"]/div[contains(@class, "zu-itemmod")]')
    #items = html.xpath('//div[@id="list-content"]/div[@_soj]')
    #print(items)
    rows = []
    for i, item in enumerate(items):
        print(i)
        item = etree.ElementTree(item)
        title = item.xpath('//div[@class="zu-info"]/h3/a/@title')[0]
        link = item.xpath('//div[@class="zu-info"]/h3/a/@href')[0]
        #print(i)
        detail = get_html(link)
        if detail:
            detail = etree.ElementTree(etree.HTML(detail))
            # 小区信息 class="cinfo"  id="commmap"
            cinfo = detail.xpath('//*[@id="commmap"]')
            if not cinfo: # 没小区信息就认为这条记录不完整，跳过
                continue
            # 房源信息 class="pinfo" //*[@id="content"]/div[2]/div[2]/div[1]/div[2]
            pinfo = detail.xpath('//*[@id="content"]/div[2]/div[2]/div[1]/div[2]')[0]
            pinfo = etree.ElementTree(pinfo)
            # 租金
            rent = pinfo.xpath('/div/div[2]/div[1]/div[1]/dl[1]/dd/strong/span[@class="f26"]/text()')[0]
            roomtype = pinfo.xpath('/div/div[2]/div[1]/div[1]/dl[3]/dd/text()')[0] # 房型
            rentway = pinfo.xpath('/div/div[2]/div[1]/div[1]/dl[4]/dd/text()')[0]  # 租赁方式
            area1 = pinfo.xpath('/div/div[2]/div[1]/div[1]/dl[6]/dd/a[1]/text()')[0] # 区域
            area2 = pinfo.xpath('/div/div[2]/div[1]/div[1]/dl[6]/dd/a[2]/text()')[0]
            deco = pinfo.xpath('/div/div[2]/div[1]/div[2]/dl[2]/dd/text()')[0]  # 装修
            mianji = pinfo.xpath('/div/div[2]/div[1]/div[2]/dl[3]/dd/text()')[0] # 面积
            face = pinfo.xpath('/div/div[2]/div[1]/div[2]/dl[4]/dd/text()')[0]  # 朝向
            type_ = pinfo.xpath('/div/div[2]/div[1]/div[2]/dl[6]/dd/text()')[0] # 住宅类型
            #print(i, rent,roomtype,rentway,deco,area2,mianji,face,type_)

            cinfo = etree.ElementTree(cinfo[0])
            comm_name = cinfo.xpath('/div/div[2]/div[2]/div[1]/dl[1]/dd/a[1]/text()')[0] # 小区名
            address = cinfo.xpath('/div/div[2]/div[2]/div[1]/dl[3]/dd/text()')[0]
            build_year = cinfo.xpath('/div/div[2]/div[2]/div[2]/dl[3]/dd/text()')[0] # 建造年代
            rj_rate = cinfo.xpath('/div/div[2]/div[2]/div[2]/dl[4]/dd/text()')[0]  # 容积率  越小越好
            green_rate = cinfo.xpath('/div/div[2]/div[2]/div[2]/dl[6]/dd/text()')[0]   # 绿化率

            #print(i,build_year,rj_rate,green_rate)
            row = title, rent, roomtype, rentway, deco, area1, area2, mianji,\
                    face, type_, comm_name, address, build_year, rj_rate, green_rate, link
            #print(row)
            rows.append(row)
        
    return rows


def save_to_csv(data, filename, mode='w'):
    with open(filename, mode, newline="") as datacsv:
    #with open("{}.csv".format(filename), "a", newline="") as datacsv: # a是追加写入
        writer = csv.writer(datacsv)
        # 写入标题
        # zip(titles, roomstyle, mianji, cenggao,niandai,price,address)
        if mode=='w':
            writer.writerow(["标题", "租金", "房型",'租赁方式', '装修','区域1','区域2',"面积",\
                '朝向', '住宅类型', "小区名", "地址", "年代","容积率","绿化率", '链接']) 
        writer.writerows(data)


def crawl_one(url):
    
    html = get_html(url)
    data = crawl_data(html)
    save_to_csv(data, 'anjuke.csv', mode='a')

def run():
    tasks = []
    url = 'https://sh.zu.anjuke.com/fangyuan/p{}/'
    for n in range(1, 10):
        tasks.append(gevent.spawn(crawl_one, url.format(n)))
    gevent.joinall(tasks)

if __name__ == '__main__':
    #url = 'https://sh.zu.anjuke.com/fangyuan/p1/'
    #crawl_one(url)
    
    run()
