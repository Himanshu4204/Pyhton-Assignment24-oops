#2. Write a python program to create a user class with a method to greet the user.?
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"Name:-{self.name} \n age:-{self.age}")
        
Obj=user("Himanshu",20)
Obj.greet()

