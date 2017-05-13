#可变参数函数
def concat(*args , sep ='/'):
    return sep.join(args);

result = concat("earth","mars","venus");
print(result);
result1 = concat("earth","mars","venus",sep =".");
print(result1);

# 参数分拆
# *args 分拆 元祖
# **args 分拆 字典
list1 = list(range(3,6))
print(list1);
args = [3,6]
list2 = list(range(*args))
print(list2);



def make_inc(n):
    return lambda x: x+n;

f= make_inc(42);
re = f(2);
print(re);
print(make_inc.__doc__)



