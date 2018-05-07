#使用__slots__
#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Student(object):
    __slots__=('name', 'age')

s = Student();
s.name = 'Michael'
s.age = 19
#s.score = 90 #AttributeError: 'Student' object has no attribute 'score'

#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：


class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 80
print(g.score) # 80 
