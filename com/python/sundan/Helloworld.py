principal =1000;
rate = 0.05;
numberY=5;
year =1;
f  = open("out","w")# 打开文件进行写入
while year <= numberY:
    principal =  principal *(1+rate)
    #print ("%3d %0.2f" %(year, principal),file = f)
    f.write("%3d %0.2f" %(year, principal))
    year +=1