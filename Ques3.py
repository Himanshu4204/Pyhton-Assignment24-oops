# 3. Write a python program to create 2 objects of the user class and assign different values.?
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        print(f"Name:{self.name} \n Age:{self.age}")

Obj1=user("Himanshu",20)
Obj2=user("Ranu",20)
Obj1.details()
Obj2.details()
