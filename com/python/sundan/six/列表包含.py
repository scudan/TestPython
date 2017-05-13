nums = [1,2,3,4,5]
squares = []

for n in nums:
    squares.append(n*n)
#print(squares)
# 列表推导
squares1 = [n * n for n in nums]
#print(squares1)

# 列表推导语法
# [expression for item1 in iter if condition1 for item2 in iter2 if condition2 .....]
a = [-3,5,3,-10,6,8]
b = 'abc'
c = [2*s for s in a]
#print(c)
d = [ s for s in a if s >= 0]
#print(d)

e = [(x,y) for x in a for y in b if x> 0]
#print()


# 生成器表达式,是一个对象,执行计算和列表相同,但会迭代的生成结果
# 语法 (expression for item1 in iter if condition1 for item2 in iter2 if condition2 .....)
a1 = [1,5,3,6]
b1 =(s*2 for s in a1)
#for ss in b1:
#    print(ss)


# 区别: 列表推到先生成列表放到内存, 生成器生成对象,只是知道如何按照需要生成数据的生成器

# 声明式编程

# lambda 可以创建表达式形式的匿名函数
# lambda args: expression
# args 是以逗号分隔的参数,而 expression 是用到这些参数的表达式
a2 = lambda  x,y : x+y
r2  = (2+3)
#print(r2)

names =["lild","Dfee","dff","dadl"]
names.sort(key=lambda  n: n.lower()) # 值全部转换为小写进行比较
#print(names)

#递归
def flatten(lists):
    for s in lists:
        if isinstance(s, list):
            flatten(s)
        else:
            print(s)

otems = [[1,2,3],[4,5,[5,6]],[7,8,9]]
flatten(otems)

def genflatten(lists):
    for s in lists:
        if isinstance(s, list):
            for item in genflatten(s):
             yield item
        else:
            yield s

otems = [[1,2,3],[4,5,[5,6]],[7,8,9]]
flatten(otems)

ff = genflatten(otems)
#print(ff.__next__())



#文档字符串

def docfunction():
    """SSSS"""
    print("sss")


cc = docfunction()

def wrapss(func):
    def calls(*ar, **kwa):
         return func(*ar, **kwa)
    calls.__doc__ = func.__doc__
    calls.__name__ = func.__name__
    calls.__dict__ .update(func.__dict__)
    return calls



#固定函数: eval(), exception(), compile()
#eval (str [, globals [,locals]]) 函数执行一个表达式字符串 并返回
a = eval('3*math.sin(3.5+x) + 7.2')

b = [3,5,10,23]

exec("for i in b: print(i)")


