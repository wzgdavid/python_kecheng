import gevent
from gevent import monkey; monkey.patch_all()
import time
def foo(n):
    
    time.sleep(3)
    print(n)
tasks = [ # 协程
    gevent.spawn(foo, 444),
    gevent.spawn(foo, 555),
    gevent.spawn(foo, 666),
    gevent.spawn(foo, 666),
    gevent.spawn(foo, 777)
]


# 没有并发
foo(123)
foo(123)
foo(123)
foo(123)
foo(123)

