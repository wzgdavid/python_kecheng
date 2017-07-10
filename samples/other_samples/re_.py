# encoding: utf-8
import re

'''
正则匹配的例子
ip
URL
邮箱地址

'''
# 两种形式，一种re.search(ptn, string)

# ip
ptn = r'^[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}$'
print re.search(ptn, '192.168.1.100')
#URL
ptn = r'^(http|https|ftp|ftps):\/\/.+'
print re.search(ptn, 'http://www.amznz.com/often-mail-domain/')
print re.search(ptn, 'http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html')
# 邮箱地址
print(re.search(r'[\w]+\@[\w]+\.(com|cn|net)$', 'wzg@sina.com'))

# 另一种形式  ptn=re.compile(ptn), ptn.search(string)
ptn = re.compile(ptn)
print ptn.search('http://www.amznz.com/often-mail-domain/')


print re.split(r'\d+', 'one1two2three3four4')

print re.sub(r'\d+', '-', 'one1two2three3four4')
