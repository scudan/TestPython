class Animal(object):
    def run(self):
        print('aimal is runing..')

class Dog(Animal):
    def run(self):
        print('dog is runing..')
    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('cat is runing..')

dog = Dog()
dog.run();

cat = Cat()
cat.run()