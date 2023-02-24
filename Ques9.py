#9. Write a python program to create a School class and 3 instance variables and 1 class variable.?
class School:
    className="12th"  #class variable
    def __init__(self,name,age,rollno):    #instance variables
        self.name=name      
        self.age=age
        self.rollno=rollno

    def show_result(self):
        print(f"Student Name:{self.name}\n Class:{School.className}\n Age:{self.age}\n Rollno:{self.rollno}")
    
Obj=School("Himanshu",20,89)
Obj.show_result()
