# 6. Write a python program to create 3 user objects and find the youngest of all.?
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user1=User("Himanshu",20)
user2=User("Ajay",25)
user3=User("Ranu",29)
# finding the youngest user object
youngest_user=user1
for user in [user2,user3]:
    if user.age < youngest_user.age:
        youngest_user=user

print(f"{youngest_user.name} is the youngest with an age {youngest_user.age}")
