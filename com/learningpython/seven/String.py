import  sys
S = "spame";
print(S.capitalize())
print("SPAME".join(["qw","ss","ddd"]))

print("%(n)d %(x)s" % {"n":5,"x":"spame"});

template = '{0},{1} and {2}';
t1 ='' ;
print(template.format('spame','ham','eggs'));

template1 = '{food},{ddd} and {d1}';
print(template1.format(food ='dd1', ddd= 'dd2',d1='dd3'))

template1 = '{food},{0} and {d1}';
print(template1.format('dd2',food =[1,42],d1='dd3'))

#占位符
print('My {1[spam]} runs {0.platform}'.format(sys,{'spam':'laptop'}))

#字典变量
print('My {config[spam]} runs {sys.platform}'.format(sys=sys,config={'spam':'laptop'}))

somelist = list('SPAM')

#变量索引
print('fisrt={0[0]},third ={0[2]}'.format(somelist))
#变量占位
print('fisrt={0},third ={1}'.format(somelist[0],somelist[-1]))

#新变量值
parts = somelist[0],somelist[-1],somelist[1:3]
print(parts)
print('fisrt={0},third ={1},middle={2}'.format(*parts))

print("ss".__dir__())




