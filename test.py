class P1:

    def m1(self):
        print("This is m1 method")


class C1(P1):

    def m2(self):
        print('This is m2 method')


class C2(P1):

    def m3(self):
        print('This is m3 method')

class C3(P1):

    def m4(self):
        print('This is m4 method')

class CC(C1):

    def m5(self):
        print('This is m5 method')


class CC2(C1, C2, C3):

    def m6(self):
        print('This is m6 method')
        




obj1 = CC2()

obj1.m1()
obj1.m2()
obj1.m3()
obj1.m4()
#obj1.m5()
obj1.m6()