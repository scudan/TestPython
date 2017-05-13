# 没有顺序的
x = set('abcde');
y = set('bdxyz');
print(x);
x.add('ddd');
print(x)
z = x.intersection(y); #  x&y
print(z);
z.update(set(['X','Y']))
print(z);
z.remove('b');
print(z);

for item in  set('abc'):
    print(item * 3);

# 新定义一个集合
S1  = {x*2 for x in (1,2,3,4)}
print(S1);

# 列表去重
L = [1,2,1,3,5,6,3]
S11  = set(L)
print(S11)
L1 = list(S11)
print(L1)