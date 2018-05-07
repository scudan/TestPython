#偏函数
import  functools
intb = int('12345',base = 8)
print(intb)
intc = int('12345',16)
print(intc)

def int2(x , base = 2):
    return int(x,base)
print(int2('1000000'))

int23 = functools.partial(int, base = 2)

print(int23('1000001'))
print(int23('1000001',base  =10))

#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
#实际把作为 *args的一部分自动加到左边
max2 = functools.partial(max, 10)
# max2(5,6,7) 相当于 args = (10, 5, 6, 7) max(*args)
