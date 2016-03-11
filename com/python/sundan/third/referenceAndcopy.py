import copy
a = [1,2,3,4]
b = a #  b引用a
print(b is a )
b [2] = 10 # a 也改变
print(a)

d = [1,2,[3,4]]
c = list(d) # 浅复制
print(c is d )
c.append(100)
print(d)
c[2][0] = -1000 # c 和 d 共享浅复制的内容,当c改变,d对应改变
print(d)

e = [1,2,[3,4]]
f = copy.deepcopy(e)
c[2][0] = -1000