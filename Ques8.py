# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted order based on the ram size. ?
class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
    
laptop1=laptop("Dell",8,"i7","500GB")
laptop2=laptop("HP",4,"i5","250GB")
laptop3=laptop("Lenovo",12,"i9","150GB")

laptops = [laptop1, laptop2, laptop3]
laptops_sorted = sorted(laptops, key=lambda laptop: laptop.ram)

for laptop in laptops_sorted:
    print(f"{laptop.brand} --Ram:{laptop.ram}GB")

