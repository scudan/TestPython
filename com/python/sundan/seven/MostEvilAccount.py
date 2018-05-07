from  EvilAccount import  EvilAccount
from  DepositCharge import  DepositCharge
from  WithdrawCharge import  WithdrawCharge
class MostEvilAccount(EvilAccount,DepositCharge,WithdrawCharge):
    def deposit(self,amt):
        print("deposit MostEvilAccount")
        #self.deposit_fee()
        super(MostEvilAccount, self).deposit(amt)
       # super(MostEvilAccount, self).deposit(amt)
    def meawithdraw(self,amt):
        print("withdraw MostEvilAccount")
        self.withdraw_fee()
       # super(MostEvilAccount, self).withdraw(amt)