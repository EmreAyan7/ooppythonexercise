#inheritance miras /kalıtım


class Person:
 
      def __init__(self,fname,lname):
            self.firstname=fname
            self.lastname=lname

      def mymethod(self):
             print(self.firstname,self.lastname)
            
class Student(Person):
      def __init__(self,year):
       
            self.graduationyear =year
      def welcome(self):
            print(f"Welcome {self.firstname}{self.lastname} to the class of {self.graduationyear}")
    

p1=Student("emre","ayan",2025)
 
p1.mymethod()
p1.welcome()
print(p1.graduationyear)

 