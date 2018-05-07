#装饰器 本质上，decorator就是一个返回函数的高阶函数

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')

now()


def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log1('execute')
def now1():
    print('2015-3-25')

# now1 = log('execute')(now1)
# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
now1()
# wrapper
print(now1.__name__)
