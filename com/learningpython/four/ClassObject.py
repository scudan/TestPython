class Worker:
    def __init__(self,name,pay):
        self.name = name;
        self.pay = pay;
    def lastName(self):
        return self.name.split()[-1];
    def giveRaise(self,percent):
        self.pay *=(1.0+percent);



Bob = Worker('Bob Delly',5000);
James = Worker('James Cammellen',6000);

print(Bob.lastName())
print(James.giveRaise(0.05));
print(James.pay)