# encoding:utf-8
import os

current_dir = os.getcwd()


def fib(n):
    '''递归的经典例子'''
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def work(dirname):
    '''
    需要知识点， 函数，if语法，递归
    '''
    for name in os.listdir(dirname):
        # os.path在windows下表示反斜杠'\'，linux下是斜杠'/'
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print path
        else:
            work(path)


def copyfile():
    '''
    需要知识， 列表，for语句
    '''
    f = open('requirements.txt', 'r')
    lines = f.readlines()
    f2 = open('tmp.txt', 'w')
    for line in lines:
        print line
        f2.write(line)
    f.close()
    f2.close()

def copyfile_with():
    with open('requirements.txt', 'r') as f:
        lines = f.readlines()
        
    with open('tmp.txt', 'w') as f2:
        for line in lines:
            f2.write(line)

def forrange():
    a= 2
    if 1:
        a = 1
    print a 
if __name__ == '__main__':
    #work(current_dir)
    #copyfile_with()
    print dict(zip([1,2],[2,3]))