class account:
    def __init__(self, balance, account_num):
        self.balance = balance
        self.account_num = account_num

    def debit(self, amount):
        self.balance -= amount
        print(f"RS", {amount}, "was debited")
        print("total_balance =", self.getbal())

    def credit(self, amount):
        self.balance += amount
        print(f"RS", {amount}, "was credited")
        print("total_balance =", self.getbal())

    def getbal(self):
        return self.balance

    


acc1 = account(10000, 234)
acc1.debit(1000)
acc1.credit(500)
acc1.debit(650)
acc1.credit(200)