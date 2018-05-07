#对象信息, 实例属性和类属性

print(type(123));
print(type('str'));
print(dir('abc'))

#下面两个是等价的
print(len('asdsda'));
print('asdsda'.__len__())


#对象想用len,需要默认第一个方法 __len__()

class Mydog(object):
    def __len__(self):
        return 100;

dog = Mydog()
print(len(dog)) # 返回100

class Myobject(object):
    def __init__(self):
        self.x = 9;
    def power(self):
        return self.x * self.x;

obj = Myobject();

print(hasattr(obj,'x'))

print(hasattr(obj,'y'))

setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print(obj.y)
print(getattr(obj,'z',190))

print(hasattr(obj,'power'))

fb = getattr(obj,'power')
print(fb())
