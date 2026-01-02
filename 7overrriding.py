class Animal:
    def speak(self):
        return "sound"
    
class Dog(Animal):
    def speak(self):   #method overriding metot ezme
        return "Bark"
    
class Cat(Animal):
    def speak(self):   #method overriding metot ezme
        return "meowww"
    

dog=Dog()
cat = Cat()

print (dog.speak())
print(cat.speak())