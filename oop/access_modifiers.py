
class User:
    name = 'salman'
    __password = '1234'
    def method1(self):
       return self.__password
class Student(User):
    pass
    # print(User().__password)


user = User()
print("this is",user.method1())
# print(user.__password)