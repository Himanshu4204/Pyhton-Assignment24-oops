#4. Write a python program to init default values for user object using __init__ method.?
class student:
    def __init__(self,name,email=None):
        self.name=name
        self.email=email

Obj=student("Himanshu")
print("Name:",Obj.name)
print("Email:",Obj.email)

