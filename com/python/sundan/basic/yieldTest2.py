import time
def tail(f):
    #f.seek(0,2) #移动到EOF
    while True:
        line = f.readline()
        if not line : #没有内容,暂时休眠并再次尝试
            time.sleep(0.1)
            continue
        yield line
def grep(lines, searchText):
    for line in lines:
        if searchText in line: yield line

wwwlog = tail(open("wwwlog.txt"))
pylines  = grep(wwwlog,"goo")
for line in pylines:
    print(line);
