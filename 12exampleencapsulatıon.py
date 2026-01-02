class Employee:
    def __init__(self,n,s):
        self.name=n
        self.__salary=s
        self._bonus=700

    def _calculatebonus(self):
        return self._bonus
    
    def __calculateSalary(self):   #private method
        return f"Salary :{self.__salary}"
    
    def getsalary(self):
        return self.__calculateSalary()

        
class Manager(Employee):
    def __init__(self, n, s,d):
        super().__init__(n, s)
        self.department = d

    def displayinfo(self):
      return f"Manager:{self.name},Department:{self.department},bonus:{self._bonus}"

    def getbonus(self):
       return f"bonus:{self._calculatebonus()}"

manager= Manager("Emre Ayan",5500,"IT")
print (manager.getsalary())
print (manager.displayinfo())
print (manager.getbonus())