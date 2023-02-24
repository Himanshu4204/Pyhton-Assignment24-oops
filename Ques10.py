#10. Define a class Employee with instance object variables empid, name, salary.
#    Write__init__() method in the class to initialize instance object variables. 
#    Also define instance methods to input fields and display field values
class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    
    def input(self):
        self.empid=input("Enter Employee ID :")
        self.name=input("Enter Employee Name :")
        self.salary=input("Enter Employee Salary :")

    def Output(self):
        print("Enployee ID:",self.empid)
        print("Employee Name:",self.name)
        print("Employee Salary :",self.salary)
    
Obj=Employee(1254,"Himanshu",12000)
Obj.input()
Obj.Output()