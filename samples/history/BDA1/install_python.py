class Foo(object):
    def bar(self):
        print('Foo.bar')
 
def bar(self):
    print('Modified bar')
 
Foo().bar()
 
Foo.bar = bar
 
Foo().bar()