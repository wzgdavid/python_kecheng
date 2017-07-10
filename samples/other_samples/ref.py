from cdeepc import A


def ref(a, newname):
    a.name = newname


if __name__ == '__main__':
    a = A()
    print a.name
    ref(a, 'newname')
    print a.name