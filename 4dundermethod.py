#dunder /magic method
class Person:
 
      def __init__(self,n,a):
            self.age=a
            self.name=n

      def __str__(self):
             return f"Name:{self.name}\nAge:{self.age}"
            
p1=Person("emre ayan",21)
 
print(p1)
 