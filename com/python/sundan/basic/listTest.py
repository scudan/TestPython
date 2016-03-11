name = ["dave","mark","Ann","phil"]
name[2] = "d222";
a = name[2];
#添加新元素
name.append("test1");
name.insert(2,"test2");
#获取链表值
name1 = name[2];
name2 = name[2:5];
## 重新赋值
name[0:2] =["tt1","tt2","tt3"];
# 链表连接
name3 = [1,2,3] + [4,5,6];
# 链表嵌套
a = [1, "ddd", 3.14,["mark", 7, 9,[1000, 101,10002]],  10];
print(a[1]);
print(a[3][2]);
print(a[3][3][2]);
#print(name3);
#print(name1);
#print(name2);
#print(name);



