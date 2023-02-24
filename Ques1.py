#Write a python program to create a user class with 3 properties: name,age,email?
class user:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
        
a=user("Himanhsu",30,'himanshurajput14504@gmail.com') 
print(f"Name:-{a.name} \n Age:-{a.age} \nemail:-{a.email}")

