class A:
    def __init__(self) :
        print('A')
    def method1(self):
        print("method1")
    def method2(self):
        print("method2")
class B(A):
    def __init__(self) :
        print('B')
    def method3(self):
        print("method3")
    def method4(self):
        print("method4")
class C(B):
    def __init__(self) :
        super().__init__()
        print('C')
    def  method5(self):
        print("5")


c=C()

c.method5()