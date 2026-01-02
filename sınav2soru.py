class Account:
    def __init__(self, hesap_no, bakiye=0):
        self.hesap_no = hesap_no
        self.bakiye = bakiye
        self.beneficiaries = [] ##para gönderebileceği hesaplar

    def add_beneficiary(self, beneficiary_account):
        if beneficiary_account not in self.beneficiaries:
            self.beneficiaries.append(beneficiary_account)
            print(f"Beneficiary {beneficiary_account.hesap_no} eklendi.")
        else:
            print(f"Beneficiary {beneficiary_account.hesap_no} zaten mevcut.")

    def transfer(self ,miktar,to_account):
        if miktar > self.bakiye:
            print("yetersiz bakiye")
            return
        self.bakiye -= miktar
        to_account.bakiye += miktar
        print(f"{miktar} {self.hesap_no} hesabından {to_account.hesap_no} hesabına transfer edildi.")
    
    def pay_bill(self, miktar, biller_account):
        if miktar > self.bakiye:
            print("fatura ödemek için yetersiz bakiye")
            return
        self.bakiye -= miktar
        biller_account.bakiye += miktar
        print(f"{miktar} fatura {biller_account.hesap_no} hesabına ödendi.")

class Customer:
    def __init__(self,isim):
        self.isim = isim
        self.accounts = []

    def login(self, account):
        self.accounts.append(account)
        print(f"Müşteri {self.isim} {account.hesap_no} hesabına giriş yaptı.")
        
    def view_accounts(self):
       for account in self.accounts:
    
        print(f"Hesap Numarası: {account.hesap_no}, Bakiye: {account.bakiye}")
    
# Örnek kullanım:
acc1 = Account("123456", 1000)
acc2 = Account("654321", 500)
customer = Customer("Alice")
customer.login(acc1)
customer.view_accounts()
acc1.add_beneficiary(acc2)
acc1.transfer(200, acc2)    
 