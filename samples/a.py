def fib(n):
    if n == 0 :
        rtn = 0
    elif n == 1 :
        rtn = 1
    else:
        rtn = fib(n-2) + fib(n-1)
    return rtn
print(fib(7))
