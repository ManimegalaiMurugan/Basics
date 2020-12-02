class Account:
    
    def __init__(self,owner,deposit):
        self.owner=owner
        self.deposit=deposit
    def __str__(self):
        
        return f'Account owner:   {self.owner}\nAccount balance: ${self.deposit}'
       
    
    def depositt(self,amount_added):
        self.deposit = self.deposit+amount_added
        print("Deposit Accepted")
    def withdraw(self,withdraww):
        if self.deposit >= withdraww:
            self.deposit = self.deposit-withdraww
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")
            

acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.deposit)
acct1.depositt(50)
acct1.withdraw(75)
acct1.withdraw(500)
