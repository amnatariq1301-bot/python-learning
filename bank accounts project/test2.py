from test import *
david = bank_account(1000, "David")
sara = bank_account(2000, "Sara")

david.get_balance()
sara.get_balance()

david.deposit(700)
sara.deposit(400)

david.withdraw(200)
sara.withdraw(3000)