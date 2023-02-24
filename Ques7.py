#7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu, hdd) and 
#   2 methods (showConfig() to print the values, __init__() to initialize the values).
class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
    
    def showConfig(self):
        print(f"Brand:{self.brand}\n Ram:{self.ram}\n cpu:{self.cpu} \nHDD:{self.hdd}")
    
Obj=laptop("Dell",'8GB',"i5","500GB")
Obj.showConfig()