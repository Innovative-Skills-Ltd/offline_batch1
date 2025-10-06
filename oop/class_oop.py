class Student:
    name = 'salman'
    email = 'sms@gmail.com'
    def __init__(self,name,email): 
        self.x = name
        self.y = email
    def display_info(self,phone):
        return self.x

name = input("enter your name: ")
email = input("enter your email")


stud1 = Student(name,email)
x = stud1.display_info('01705644008')
print(x)

