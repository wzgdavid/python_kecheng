import gevent
from gevent import monkey; monkey.patch_all()
import time

def foo(n):
    print(n)
    time.sleep(5)  # 好比服务器的响应时间
tasks = [
    gevent.spawn(foo, '123'),
    gevent.spawn(foo, '124'),
    gevent.spawn(foo, '125'),
    gevent.spawn(foo, '126'),
    gevent.spawn(foo, '127')
]
#gevent.joinall(tasks)

# 不用并发，费时
foo('567')
foo('567')
foo('567')
foo('567')
foo('567')