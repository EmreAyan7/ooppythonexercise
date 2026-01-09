
class Person:
 
      def __init__(self,n,a,g):
            self.age=a
            self.name=n
            self.gender=g

      def mymethod(self):
             print(f"Hello my name is {self.name}")
             print(f"ı m {self.age} years old")
             print(f"my gender is {self.gender}")
            
p1=Person("emre ayan",21,"man")

p1.age=15
 
p1.mymethod()

print(p1.age)
 