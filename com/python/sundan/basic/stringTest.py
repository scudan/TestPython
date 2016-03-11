a = 'python 1 ';
b = "python 2 ";
c = """ python '3' """;
d = ''' python '4' ''';
e = ''' "pythons'" 5 ''';
print (a);
print (b);
print (c);
print (d);
print (e);

a1 =a[4];
a2 =a[2:5];
a3=a[:2];
a4 = a[2:];
print(a1);
print(a2);
print(a3);
print(a4);
print ('--------------------------------------------')
f = '''adadw
ad333
ada
<a href = "http://adad222.org">''';
print(f);


x = "32";
y= "34";
z = x + y;
print(z);

z1 = int(x)+int(y);
print(z1);

x2 = 3.4
s = "The value of x1 is : " + str(x2);
print(s);
s = "The value of x2 is : " + repr(x2);
repr(x2);
print(repr(x2));
s = "The value of x3 is : " + format(x2,"%4d");
print(s);