class BankAccount:
    def __init__(self,a_n,b):
        self.accountnumber=a_n
        self.__balance=b

    def deposit(self,amount):
      
      if(amount>0):
         self.__balance += amount

         return f"Deposited:{amount} New balance:{self.__balance}"
      return "ınvalıd deposit amount"
    

    def __display_balance(self):
       return f"Balance:{self.__balance}"
    
    def get_balance(self):
       return self.__display_balance()
    

account = BankAccount("123445",1000)

print(account.deposit(100))

print(account.get_balance())
      
        