from math import  pi
squares = [x**2 for x in range(10)]
print (squares);

squares1 =[(x,y) for x in[1,2,3] for y in[1,2,3] if x != y]
print(squares1)
squares2 = [str(round(pi,i)) for i in range(1,6)];
print(squares2)

#嵌套列表推到方式
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

#大循环, for i in range(4)
#每一行的第 i 列 组合成一个新的元祖
squares3 = [[row[i] for row in matrix] for i in range(4)]
print(squares3)
# 等同于如下的格式
squares4 = []

for i in range(4):
     squares4.append([row[i] for row in matrix]);

print(squares4);

squares5 = list(zip(*matrix));
print(squares5)