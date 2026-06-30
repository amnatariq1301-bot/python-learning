class balanceException(Exception):
    pass

class bank_account():
    def __init__(self, balance, account_name):
        self.balance = balance
        self.name = account_name
        print(f"\n Account {self.name} created \n balance : ${self.balance : .2f}")

    def get_balance(self):
        print(f"\n Account '{self.name}' has ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit Complete")
        self.get_balance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return 
        else:
            raise balanceException(f"\n Sorry ! Account '{self.name}' has balance only ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("withdraw completed")
            self.get_balance()
        except balanceException as error:
            print(f"\n withdraw interupted : {error}")
        