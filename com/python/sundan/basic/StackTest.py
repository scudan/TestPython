class StackTest(object): #继承Object
    def __init__(self):
        self.stack = []
    @staticmethod
    def push(self,obejct):
        self.stack.append(object)
    def pop(self):
        return self.stack.pop();
    def length(self):
        return len(self.stack)


s = StackTest();
s.push("Deved");
s.push(34);
s.push([3,4,5]);
x = s.pop();
y = s.pop();
print(x);
print(y);
del s;