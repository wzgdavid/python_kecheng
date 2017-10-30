import gevent
from gevent import monkey;monkey.patch_all()
import time
def foo(n):
    time.sleep(2)
    print(n)
    
tasks = [
    gevent.spawn(foo, '123'),
    gevent.spawn(foo, '233'),
    gevent.spawn(foo, '234'),
    gevent.spawn(foo, '345'),
    gevent.spawn(foo, '456'),
    gevent.spawn(foo, '567')
]

gevent.joinall(tasks)
#foo('123')
#foo('123')
#foo('123')
#foo('123')
#foo('123')
#foo('123')