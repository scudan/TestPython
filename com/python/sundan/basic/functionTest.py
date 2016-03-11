def remainder(a,b):
    q = a//b; # 截断除余
    r = a - q*b;
    return (q,r) ;

#返回列表
quot,result = remainder(37,15);
print(quot,result);

# 参数默认值
def connect (host,port,timeout = 2000):
    print(host,port);
    
#两种调用方式
connect("10.78.65.34","8080");
connect(port="ddd",host="10.23.3.3");