a=  4 //3
#print(a)

b  = 7 % 5
#print (b)

c = 2 >> 3
#print(c)



al = [2,3,4]
bl = [al]
cl = 4 * bl
#dl = [list(a) for j in range(4)]
#print(cl)
#print(dl)
#[[2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4]]

al[0] = -3  # b 复制 a , c 是 b的 副本,修改a 则所有的都会修改

#print(cl)
###[[-3, 3, 4], [-3, 3, 4], [-3, 3, 4], [-3, 3, 4]]

items = [3,4,5]
x,y,z = items


letter = "addd"
x1,x2,x3,x4 =letter

dd = [1,2,3,4,5]

dd[2:4] =[10,33]
print(dd)
#[1, 2, 10, 33, 5]
dd[3:4] = [-3,-4,-2]
print(dd)
# 扩展结果
# [1, 2, 10, -3, -4, -2, 5]
dd[2:] = [0]
print(dd)
#[1, 2, 0]
# 使用步进参数时,右面数值必须和左边替换值一样

