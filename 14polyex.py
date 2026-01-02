class Employee:
    def __init__(self,name):
        self.name=name
    def calculate_salary(self):
        raise NotImplementedError ("subclasses must implement this method!")
    
class Mounthly(Employee):
    def __init__(self, name,mounthly_salary):
        super().__init__(name)
        self.mounthly_salary=mounthly_salary
    def calculate_salary(self):
        return self.mounthly_salary
    
class Hoursly(Employee):
    def __init__(self, name,hourly_rate,hworked):
        super().__init__(name)
        self.hourly_rate=hourly_rate
        self.hoursworked=hworked

    def calculate_salary(self):
        return self.hourly_rate*self.hoursworked
    
class Freelancer(Employee):
    def __init__(self, name,projectrate,completedproject):
        super().__init__(name)
        self.projectrate=projectrate
        self.completedproject=completedproject

    def calculate_salary(self):
        return self.projectrate*self.completedproject

employee= [Mounthly("EMRE",8000),Hoursly("Ahmed",50,5),Freelancer("nazlı",500,5)]

for x in employee:
   print (f"{x.name}:{x.calculate_salary()}")