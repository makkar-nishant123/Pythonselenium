
class A(object):
    @classmethod
    def test1(cls):
        print ("Class A : test1 - method name")


    def test2(self):
        print("Class A : test2 - method name")

class B(object):
    def test1(self):
        print("Class B : test1 - method name")

    @classmethod
    def test2(cls):
        print("Class B : test2 - method name")

class C(object):

    def testing(self):
        print("Testing class C")
#B = B()
# B.test1()
# B.test2()
testing1 = "Test"

#A = A()
# A.test1()
# A.test2()

C= C()
# C.testing()