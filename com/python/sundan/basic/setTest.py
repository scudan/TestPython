s = set([3,5,6,8,9,10]);
t = set(["Hello"]);

t.add('x')
t.update([10,30,43])
a = s | t;
b = s & t;
c = s - t;
d = s ^ t;
print(a);
print(b);
print(c);
print(d);