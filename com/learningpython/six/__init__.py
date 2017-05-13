import sys
x= 6;
y = x
sys.getrefcount(x)
print(sys.getrefcount(x));
print('-'*8)

S = 'Hello';
S1 = S[::-1];
print(S1)

print(ord('s'));
print(chr(112));
print('This is %d %s bird!' % (1, 'dead'))
print('This is {0} {1} bird!'.format(1,'dead'))
