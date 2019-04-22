class Myclass(object):

    x  = 5

    def inst_method(self):
        print("My instance method")

    @classmethod
    def method1(cls):
        print(cls.x)
        #cls.inst_method() #- Work instance method for the class method


obj1  = Myclass()
obj1.method1()


Myclass.method1()

