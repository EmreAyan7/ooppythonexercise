
class Person:
 
      def __init__(self,n,a):
            self.age=a
            self.name=n

      def mymethod(self):
             print(f"Hello my name is {self.name}")
             print(f"ı m {self.age} years old")

            
p1=Person("emre ayan",21)

p1.age=13
 
p1.mymethod()

print(p1.age)
 