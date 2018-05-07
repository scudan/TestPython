#修正函数名
import  functools, time

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.clock()
        print("---- %s ---- begin" % func.__name__)
        vv = func(*args, **kw)
        print("---- %s ---- end" % func.__name__)
        end = time.clock()
        print('call %s():, xecuted in %s ms' % (func.__name__, end - start))
        return vv;
    return wrapper

def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.clock()
        print("---- %s ---- begin" % func.__name__)
        vv = func(*args, **kw)
        print("---- %s ---- end" % func.__name__)
        end = time.clock()
        print('call %s():, xecuted in %s ms' % (func.__name__, end - start))
        return vv;
    return wrapper

@log
def now1():
    print('2015-3-25')
#修正函数名
print(now1.__name__)
now1()