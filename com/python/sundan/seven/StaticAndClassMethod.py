class Foo(object):
    @staticmethod
    def add(x,y):
        return x+y


d = Foo.add(3,5)
print(d)