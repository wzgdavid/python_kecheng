def power(a, n=2):
    aa = not isinstance(a, (int, float))
    nn = not isinstance(n, (int, float))
    if aa or nn:
        raise TypeError('need int or float')
    return a**n

print(power('4',3))