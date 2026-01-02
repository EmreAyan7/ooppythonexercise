class Animal:
    def __init__(self,n,s):
         self.name=n       #public
         self._species=s    #türü protected property
   
    def _display(self):  #protected method
         return "Animal sound"
    

class Dog(Animal):
     def __init__(self, n, b):
          super().__init__(n,"Dog")
                              
          self.breed = b      #protected diğer classlarda kullanmak icin daha ideal
  
     def display_info(self): #public methoc
          return f"dog name: {self.name}, dog species is: {self._species}, breed:{self.breed} "
     def make_sound(sound):
          return self_makesound()
     

dog = Dog("kURT","Golden retriever")

print (dog.display_info())

print(dog._display()) #protected boyle kullanılıyor ama dogru degıl 

