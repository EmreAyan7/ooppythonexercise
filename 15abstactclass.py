from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
                #if ı use Shape class in another class we must use this two method.(inheritance)
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,x,y):
        self.width=x
        self.height=y

    def area(self):
        return self.height*self.width
    
    def perimeter(self):
        return 2*(self.height+self.width)
    
class Circle(Shape):
    def __init__(self,r):
        self.radius=r

    def area(self):
        return self.radius**2*3.1415
    
    def perimeter(self):
        return 2*3.1415*self.radius
    
daire=Circle(10)
print(f"ucgen alanı : {daire.area()}, çevresi:{daire.perimeter()}")

dikdörtgen=Rectangle(10,5)
print(f"dikdortgen alanı : {dikdörtgen.area()}, çevresi:{dikdörtgen.perimeter()}")
