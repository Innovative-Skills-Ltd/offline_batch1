

class A:
    def __init__(self):
        print("this is parent class constructor")
    def sample_method(self):
        print("this is parent sample method")

class A1(A):
     def sample_method(self,x):
        #A().sample_method()
        super().sample_method()
        print(x)
        print("this is child sample method")

a1 = A1()

a1.sample_method(10)


