class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index ==0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]


rev = Reverse("test");

#调用class 中的iter 及 next
for cahr in rev:
    print(cahr)


print("----------------------------------------------")
# 生成器

def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield  data[index]

for cahr in reverse("gloable"):
    print(cahr)
print("+++++++++++++++++++++++++++++++++++++++++++")

data = "spame"
l11 = list(data[i] for i in range(len(data) -1 ,-1,-1))
print(l11)
