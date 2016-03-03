f = open("Helloworld.py")
line = f.readline();
while line:
    print(line),
    line = f.readline();
f.close();