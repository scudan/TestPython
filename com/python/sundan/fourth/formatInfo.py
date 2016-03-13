a = 42
b = 13.148322
c = 'hello'
d = {'x':13,'y':1.54321,'z':'world'}
e = 223232131231231

r = "a is %d" % a
print(r)
r = "%10d %f" % (a,b)
print(r)
r = "%+010d %E" % (a,b)
print(r)
r = "%(x)-10d %(y)0.3g" % d
print(r)
r = "%0.4s %s" %(c, d['z'])
print(r)
r = "%*.*f" %(6,4,b)
print(r)
r = "e = %d" %e
print(r)

#rr 是一个字典
name = "eeellll"
age = 32
r = "%(name)s is %(age)s  year old" % vars()
rr = vars();
print(rr['name'])
