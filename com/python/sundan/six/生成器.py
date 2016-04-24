# 使用yield 定义生成器对象, 生成器是一个函数,生成一个值得序列,以便在迭代中使用
def countdown(n):
    print("Counting down from %d" % n)
    while n > 0:
        yield n
        n -= 1
    return

c = countdown(10)
print(c.__next__())  #10
print(c.__next__())  #9
# 调用next,生成器函数不断执行语句,直到遇到yield为止,yield在函数执行停止的地方生成一个结果,
# 直到再次执行next.然后继续执行yield后面的语句

for n in c:
    print(1+ n)



#####协程和yield#######
#yield 作为赋值运算符的右边表达式

def reciver():
    print("ready to reciver")
    while True:
        n = yield
        print("Go %s" % n)


c = reciver();
c.__next__() #执行yield的上一句, 即打印:ready to reciver, 这时协程挂起,等待c的send方法给它发送一个值

#执行前,必须执行 上面的语句 c.__next__()
c.send(1) # 接收到值,协程执行语句,直到遇到下一个yield语句,执行yield语句,且把参数传递给对应的yield对象. 本句打印:Go 1
c.send("test yield! ") # 执行yield语句,且把参数传递给对应的yield对象. 本句打印:Go test yield!

# 使用装饰器,保证c.__next__()不被漏执行
def contr(func):
    def start(*ar1, **arg2):
        g  = func(*ar1, **arg2)
        g.__next__()
        return g
    return start

@contr
def reciver1():
    print("ready to reciver1")
    while True:
        n = yield
        print("Go1 %s" % n)


r = reciver1() # 打印ready to reciver1
r.send(11) # 打印Go1 11



# 同时处理输入和输出
def line_splitter(delimiter=None):
    print("Ready to split!")
    result = None
    while True:
        line = (yield result)
        result = line.split(delimiter)

ls = line_splitter(",")
ls.__next__(); # 执行到yield ,返回result的初始值 None
result1 = ls.send("ab,c")#拆分到result, send 返回值就是传递给下一条yield语句的值
print(result1)
