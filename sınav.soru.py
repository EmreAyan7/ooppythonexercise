class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.beneficiaries = []
    
    def add_beneficiary(self, beneficiaries_account):
        if beneficiaries_account not in self.beneficiaries:
            self.beneficiaries.append(beneficiaries_account)
            print(f"Beneficiary {beneficiaries_account.account_number} added.")
        else:
            print(f"Beneficiary {beneficiaries_account.account_number} already exists.")

    def transfer(self, amount, to_account): 
        if amount > self.balance:
            print("Insufficient funds for the transfer.")
            return
        self.balance -= amount
        to_account.balance += amount
        print(f"Transferred {amount} from {self.account_number} to {to_account.account_number}.")

    def pay_bill(self, amount, biller_account):
        if amount > self.balance:
            print("Insufficient funds to pay the bill.")
            return
        self.balance -= amount
        biller_account.balance += amount
        print(f"Paid {amount} to biller {biller_account.account_number}.")

        
class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    
    def login(self, account):
        self.accounts.append(account)
        print(f"Customer {self.name} logged into account {account.account_number}.")

    def view_accounts(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Balance: {account.balance}")


# Example usage:
acc1 = Account("123456", 1000)
acc2 = Account("654321", 500)

customer = Customer("Alice")

customer.login(acc1)
customer.view_accounts()

acc1.add_beneficiary(acc2)
acc1.transfer(200, acc2)