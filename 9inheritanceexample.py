class Car:
    def __init__(self,brand,model,fueltype,capacity):
       self.fueltype = fueltype
       self.model =model
       self.brand=brand
       self.capacity =capacity
       self.fueltype=fueltype
       

    def start (self):
        return f"{self.brand},{self.model} is start"
    
    def stop (self):
        return f"{self.brand},{self.model} is stopping"
    
class Petrolcar(Car):
    def refuel(self):
        return f"{self.brand},{self.model} is refuelling with petrol.Capacity :{self.capacity}L"
    
class Electricitycar(Car):
    def charge(self):
        return f"{self.brand},{self.model} is charging.Battery Capacity :{self.capacity}kWh"
    

car_p=Petrolcar("skoda","supperb","petrol",50)
car_e=Electricitycar("tesla","model3","electric",76)

print(car_p.start())
print(car_e.charge())

        