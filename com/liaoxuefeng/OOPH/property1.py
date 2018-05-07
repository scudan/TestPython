class Student(object):

    @property
    def score(self):
        return self._score;

    @score.setter
    def scor(self, value):
         if not isinstance(value, int):
            raise ValueError('score must be an integer!')
         if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
         self._score = value


s = Student()
s._score=60 # 调用setter方法
print(s._score)