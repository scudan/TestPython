import  weakref,gc

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return  str(self.value)


a = A(10)
d = weakref.WeakKeyDictionary()

d['prim'] = a
#print(d['prim'])
del a
gc.collect()

print(d['prim'])