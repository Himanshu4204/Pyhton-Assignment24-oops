#Write a python program to delete the age property of the user?
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age

Obj=user("Himanshu",20)
del Obj.age    #delete the age

print(Obj.name)
print(Obj.age)


