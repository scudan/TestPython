def power(x):
    return x * x;


#1. 带默认参数
#一是必选参数在前，默认参数在后，否则Python的解释器会报错
#有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
#也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值
def power(x,n=2):
    s = 1;
    while n > 0:
        n = n-1;
        s = s*x;
    return s;
print(power(6,3))


#2.可变参数
#在函数内部，参数numbers接收到的是一个tuple
def cal(* numbers):
    summ = 0;
    for n in numbers:
        summ = summ + n * n;
    return summ;

print(cal(1,2,3));

#如果是list伙tuple
nums = [1,3,4]
#使用下面两种调用方式
nums1 = cal(nums[0], nums[1],nums[2])
nums2 = cal(*nums)
print(nums1, nums2)


#3.关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def person(name,age, **kv):
    print('name: ', name , 'age:',age,'other: ',kv);

person('sundan',30)

person('sundan1',35,city='beijing',job='engineer')

extra = {'city': 'chengdu', 'job': 'Engineer'}
person('Jack', 24, **extra)


#4.命名关键字参数
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
#*后面的参数被视为命名关键字参数
def person1(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)
#以下接口调用报错
#person2('sundan',23,'dd','vc')
#正确调用方式
person2('sundan',23,city='dd',job='vc')

#命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *, city='成都', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')

#5.参数组合
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)



args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
#a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
#a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}