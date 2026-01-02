class Shape:
    def area(self):
        pass

class circle(Shape):
    def __init__(self,r):
       self.radius=r
    
    def area(self):
        return 3.14*self.radius**2
    
class Triangle(Shape):
    def __init__(self,b,h):
        self.base=b
        self.height=h

    def area(self):
        return self.base*self.height*0.5
                                  #hepsinde area farklı çalısıyor bu polimorfizim
class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
       return  self.side**2

shapes=[circle(5),Triangle(19,4),Square(7)]

for x in shapes:
    print (f"Area: {x.area()}")
        

