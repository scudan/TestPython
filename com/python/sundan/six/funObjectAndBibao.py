def callf(func):
    return func()

def helloworld():
    return "lll"

print(callf(helloworld))
#将组成函数的语句和语句执行的环境打包在一起时,得到的对象称为闭包

def page(url):
    def get():
        return "Hello "+url;
    return get;

gpyhton = page("http://www.baidu.com")
jpython = page("http://www.huawei.com")

print("gpython--->" + gpyhton())
print("conments--->"+ gpyhton.__closure__[0].cell_contents)
print("jpython--->" + jpython())

# 保持状态,使用闭包
def countdown(n):
    def next():
        nonlocal n
        r = n
        n -=1
        return r
    return next

next = countdown(10)
while True:
    v = next()
    print(v)
    if not v : break
