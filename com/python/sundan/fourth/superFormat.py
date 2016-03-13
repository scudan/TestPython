r = "{name} is {age}  year old".format(name = 'dees',age = 34)
print(r)
r = "{0} is {age}  year old".format('dees',age = 34)
print(r)
r = "use {{and}} ssss".format()
print(r)

# 字典变量
stock = {'name':'google', 'shares':100, 'price': 323.22}
r = "{0[name]} and {0[shares]} and {0[price]}".format(stock)
print(r)

d = {}
d[1,2,3] = "foo"
# 键值为(1,2,3)

# 条件表达式
def mins(a1,b1):
 c1 = a1 if a1 <=b1 else b1
 return c1

dd = mins(3,5)
print(dd)