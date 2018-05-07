class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' %(self.__name, self.__score))

    def get_name(self):
        return self.__name;

    def get_score(self):
        return self.__score;

    def set_name(self, name):
        self.__name = name;

    def set_score(self, score):
        self.__score = score;



bart = Student('Test01',89)
bart.print_score()
# 私有属性,不能直接访问
bart.set_name('sundan1')
print(bart.get_name())
bart.__name = 'sundan'
bart.print_score()
print(bart.get_name())
