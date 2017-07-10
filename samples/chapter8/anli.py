from urllib import request, error
from lxml import etree
import json

def get_html(url):
    try:
        response = request.urlopen(url)
        #response = request.urlopen(req)
    except error.URLError as e:
        print(e)
    except error.HTTPError as e:
        print(e)
    html = response.read().decode('utf-8')
    with open('sample.html', 'w') as f: # 第一次执行，保存为本地文件
        f.write(html)
    return html


def local_html():
    # 先用本地文件跑，等程序写完了，再从网站爬取
    with open('sample.html', 'r') as html:
        html = html.read()
    return html


def crawl_data(html):
    #html = etree.fromstring(html) # 这是个简单粗暴的方法，容易出错
    html = etree.HTML(html)
    html = etree.ElementTree(html)
    # 只要这部分html
    
    content_html = etree.ElementTree(html.xpath('//ul[@id="thread_list"]')[0])
    
    titles = content_html.xpath('//li[@class=" j_thread_list clearfix"]//a[@class="j_th_tit "]/text()')
    authors = content_html.xpath('//li[@class=" j_thread_list clearfix"]//span[@class="frs-author-name-wrap"]/a/text()')
    last_reply = content_html.xpath('//li[@class=" j_thread_list clearfix"]//span[@class="tb_icon_author_rely j_replyer"]/a/text()')
    
    print(len(titles))   # 打印长度看看是否匹配
    print(len(authors))
    print(len(last_reply))

    # 打印数据
    data = zip(titles, authors, last_reply)
    rtn = []
    for n in data:
        #print(n)
        rtn.append(n)

    next_page = html.xpath('//a[@class="next pagination-item "]/@href')

    if next_page:
        next_page_url = next_page[0]
        print(next_page_url)
    else:
        raise Exception('this is the last page')
    
    return rtn

def save_to_json(data, filename):
    with open('{}.json'.format(filename), 'w') as json_file:
        json_file.write(json.dumps(data))

def read_from_json(filename):
    with open('{}.json'.format(filename), 'r') as json_file:
        data = json.load(json_file)
    return data

def _test():
    url = 'http://tieba.baidu.com/f?kw=python'
    #url = 'http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=29150'
    html = get_html(url)
    #html = local_html()  # 先用本地保存的html边调试边写代码
    data = crawl_data(html)
    save_to_json(data, 'tieba')

    #data = read_from_json('tieba')
    #print(data)

if __name__ == '__main__':

    _test()