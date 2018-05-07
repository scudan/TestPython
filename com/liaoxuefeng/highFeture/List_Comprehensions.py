import os
#列表生成式
print(list(range(1,11)))

for x in range(1,11):
    print(x*x)
listt = [x*x for x in range(1,11)]

print(listt)

list1 = [x*x for x in range(1,11) if x%2 == 0]
print(list1)

list2 =[m + n for m in 'ABC' for n in ('XYZ')]

print(list2)

listos = [d for d in os.listdir('.')]
print(listos)

list3 = ['Hello','World','IBM','Apple']
list4 = [s.lower() for s in list3]
print(list4)