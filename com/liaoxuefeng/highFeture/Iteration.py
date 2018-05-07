from collections import  Iterable
d= {'a':1,'b':2,'c':3,'d':4}

for key in d:
    print(key, d.get(key))

for k,v in d.items():
    print("key:"+k,v);

for ch in 'ABCD':
    print(ch)


print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))

for i, va in enumerate(['A','b','d']):
    print(i, va)
print("-"*10)

for x, y in [(2,4),(3,9),(4,16)] :
    print(x,y)


minMax = [34,44,-22,47,45,23]
minMax1 = []
minMax2 = [7,7]
minMax3 =[7,1]
minn=0 ;
maxn= 0
num = 0
for num in minMax3:
    indexx = minMax3.index(num)
    temp = num
    print(temp)
    if indexx == 0 :
        minn = num;
        maxn = num
    else:
        if minn> num:
            minn = num
        if maxn < num:
            maxn =num
    print(minn, maxn)