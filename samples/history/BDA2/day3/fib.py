#def fib(n):
#    if n == 0:
#        rtn =0
#    elif n == 1:
#        rtn = 1
#    else:
#        rtn = fib(n-1) + fib(n-2)
#    return rtn
#print(fib(0))

def fib(n):
    a, b = 0, 1
    while n:
        a, b, n = b, a+b, n-1
        print(a, b, n)
    return a

print(fib(4))