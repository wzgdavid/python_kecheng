class Base():
    x = 'base'

class A(Base):
    pass

class B(Base):
    x = 'b'

#print(A.x)
print(B.x)

class C(A, B):
    pass

print(C.x)