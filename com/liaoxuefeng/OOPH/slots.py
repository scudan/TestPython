class Student(object):
    pass

s = Student()

s.name ="Test"

print(s.name)


def set_age(self, age):
    self.age = age

from types import MethodType
# 设置变量为函数
s.sa = MethodType(set_age, s)

s.sa(100)
print(s.age)
#给一个实例绑定的方法，对另一个实例是不起作用的

#为了给所有实例都绑定方法，可以给class绑定方法

def set_score(self, score):
    self.score = score;

Student.set_score = set_score

s.set_score(30)
print(s.score)

s2 = Student();
s2.set_score(70)
print(s2.score)

