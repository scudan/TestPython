L = [12,'apm',1.2];
#列表操作
print(len(L));
print(L[0]);
print(L[:-1]);
print(L+[3,4,6]);
print(L);
#类型特定操作
#添加一个元素
L.append('ssss');
print(L);
#弹出索引位置的元素
print(L.pop(2));
#弹出后,列表改变
print(L);
# 列表的详细操作
print(dir(L))

#  改变列表的方法
M = ['bb','aa','dd'];
M.sort();
print(M)
M.reverse();
print(M);


#边界检查
#检查越界


#嵌套 - 多维数组 -矩阵

M1 = [[1,2,3],[4,5,6],[7,8,9]];
print(M1)
print(M1[1])
print(M1[1][1])

# 列表解析
# 提取列值
# 把矩阵M中的每个row中的row[1] 放到1个新列表
## 个人理解,每个M中元素是一个列表,赋值给变量row,然后再使用row[1]操作
col2 = [row[1] for row in M1]
print(col2)


col3 = [row[1]+1 for row in M1 ]
print(col3);
col4 =[row[1] for row  in M1 if row[1]%2 ==0]
print(col4)


diag = [M1[i][i] for i in [0,1,2]]
print(diag)
doub = [c*2 for c in 'spma'];
print(doub);

#求其中一个子列的和
G = (sum(row) for row in M1);
print(next(G)); # 第一个子列
print(next(G)); # 第二个子列
print(next(G)); # 第三个子列
#返回所有的值
list1 = list(map(sum,M1));
print(list1)

# 创建集合
print({sum(row) for row in M1})
# 创建字典
print({i:sum(M1[i]) for i in range(3)});



