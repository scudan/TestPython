#元组 () ,支持任意类型,任意嵌套,以及常见的序列操作

T = (1,2,3,4,5);
print(len(T));
T1 = T+(6,7);
print(T1);
print(T[0]);
print(dir(T));
T2=T+(1,3)
print(T2);

# index为4的值
Tindex = T2.index(4);
print(Tindex)
# 3 出现的次数
Tcount=T2.count(3)
print(Tcount);

T3 = ('spam',3.0,[11,'age', 4.0])
print(T3[1]);
print(T3[2][1]);