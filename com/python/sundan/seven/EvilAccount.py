import random
from Account import Account
class EvilAccount(Account):
    def __init__(self,name,balance,fac):
        Account.__init__(self,name,balance)
        self.fac = fac
    def inquiry(self):
        print("evil in")
        if random.randint(0,4) == 1:
            return self.balance
        else:
            return self.balance * self.fac
