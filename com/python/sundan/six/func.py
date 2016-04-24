a = 34
b = 43

def foo():
    global a # 定义全局变量
    a = 13
    b = 0
print(a)
print(b)

# 函数嵌套
def countdown(start):
    n = start
    def display():
        print("T-MINUS %d" % n)
    def dec():
        nonlocal n  # 绑定到外边变量
        n -= 1
    while n > 0:
        display()
        dec()

countdown(5);