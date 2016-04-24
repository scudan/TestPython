#装饰器是一个函数,主要用于包装另一个函数或类,主要目的是要透明的修改和增强被包装对象的行为
# 表示装饰器语法为特殊符号 @

@trace
def square(x):
    return x*x;
#或者如下

# def square(x):
#     return x*x;
#square = trace(square);

#多个一起用,根据先后顺序使用
@foo
@bar
def addd(x):
    pass

#addd = foo(bar(addd))

# 装饰器可以接受参数
@eventHandler('BUTTON')
def handler_button(msg):
    pass

@eventHandler('RESET')
def handler_reset(msg):
    pass

#语义如下:
def handler_button(msg):
    pass
temp = eventHandler('BUTTON')
handler_button = temp(handler_button)
