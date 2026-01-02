class Flyingcar:
    def fly(self):
        return "this car flying"

class watercar:
    def sail(self):
        return "this car sail on water"

class amphibiouscar(Flyingcar,watercar):
    def drive(self):
        return "this car can also drive on the land"
    
car =amphibiouscar()
print(car.fly())
print(car.sail())
print(car.drive())