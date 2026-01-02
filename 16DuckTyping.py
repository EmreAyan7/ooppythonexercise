class Duck: 
    def quack(self):
        print ("quack cuack!")
    def fly(self):
        print("Duck is flying")

class Airplan: 
    def quack(self):
        print ("I pretending to be a duck Quack quack!")
    def fly(self):
        print("Air plan is taking off")   #duck typing polymorpihisim olmadan aynı method kullanmalarıdır.kalıtım olmadan polymorpihsm

def duck_typing(obj):
    obj.quack()
    obj.fly()

duck=Duck()
ucak=Airplan()

duck_typing(duck)
duck_typing(ucak)