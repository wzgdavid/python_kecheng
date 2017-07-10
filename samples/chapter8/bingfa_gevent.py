import gevent
from gevent import monkey; monkey.patch_all()
import time

def foo(n):
    time.sleep(5)
    print(n)
#
#
tasks = [
    gevent.spawn(foo, '123'),
    gevent.spawn(foo, '123'),
    gevent.spawn(foo, '123'),
    gevent.spawn(foo, '123'),
    gevent.spawn(foo, '123')
]

gevent.joinall(tasks)

# 不用并发，费时
foo('123456789')
foo('123456789')
foo('123456789')
foo('123456789')
foo('123456789')