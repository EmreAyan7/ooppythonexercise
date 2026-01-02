class Vehicle:
     def __init__(self,brand,model,color): #constructer method
          self.brand=brand  #instance variable
          self.model=model
          self.color=color

car1_obj=Vehicle("skoda","superb","White")
car2_obj=Vehicle("bmw","m4","red")

print(car1_obj.brand,"-",car1_obj.model,"-",car1_obj.color)
print(car2_obj.brand,"-",car2_obj.model,"-",car2_obj.color)