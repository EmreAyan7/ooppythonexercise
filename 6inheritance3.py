class person:
    
    def __init__(self,name,lname):
        self.name=name
        self.lname=lname

    def bilgi(self):
        print (self.name , self.lname)

class student(person):

   def __init__(self,name,lname,year):
     super().__init__(name,lname)
     self.graduationyear =year
    
   def welcome(self):
        print(f"welcome {self.name} {self.lname} your group is {self.graduationyear}")


person1=student("Emre","Ayan",2030)

print(person1.name)
person1.welcome()