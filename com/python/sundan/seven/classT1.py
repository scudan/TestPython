# from classTest import Account
# from EvilAccount import EvilAccount
from MostEvilAccount import MostEvilAccount
# a = Account("ddd",1000.00) ##调用Account.__init__(a,"ddd",1000.00)
# a.spam(101) #调用Account.deposit(a,100)
# print(a.balance)
#
# e = EvilAccount("eeee",1001,1.10)
#
# e.deposit(102)
# av = e.inquiry()


mea = MostEvilAccount("meeee",1001,1.10)
mea.deposit(12)
mav = mea.inquiry()
print(mea.name)
print(mav)