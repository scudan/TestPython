#file

f = open('data.txt','w');
f.write('hello\n');
f.write('world!\n');
f.close();

f1 = open('data.txt'); # like open('data.txt','r')
text = f1.read(); # 整个文件
print(text)
liist = text.split();
print(liist);
f1.close();