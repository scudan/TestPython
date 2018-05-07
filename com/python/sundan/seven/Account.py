#继承基类 object
class Account(object):
    num_accounts = 0
    def __init__(self,name,balance):
        self.name = name;
        self.balance = balance;
        Account.num_accounts +=1
    def __del__(self):
        Account.num_accounts -= 1
    def deposit(self,amt):
        self.balance  = self.balance + amt
    def withdraw(self,amt):
        self.balance = self.balance - amt
    def inquiry(self):
        print("acc in")
        return self.balance
    # 类中没有范围
    def spam(self, aa):
        # 错误语法
        #deposit(self,aa)
        #正确
        self.deposit(aa)
        #Account.deposit(self,aa)
