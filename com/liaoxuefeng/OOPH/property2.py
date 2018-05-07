#birth是可读写属性，而age就是一个只读属性
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

s = Student()
s._birth = 2000
#s.age = 23 # 只读属性
print(s._birth)
print(s.age)