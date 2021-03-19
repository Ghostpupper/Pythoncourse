class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(C, B):
    pass

d = D()