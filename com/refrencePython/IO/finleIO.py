#r - 只读
#w - 只写
#a - 追加打开
#r+ - 读写方式
f = open('test.txt','r+')
f.write('Test1')
print(f.read())
f.close();

with open('test.txt','r') as fs:
    filedata = fs.read();
    print(filedata)
fs.close()
# pickle 文件中str和实际对象的转换