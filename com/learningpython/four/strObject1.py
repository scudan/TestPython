S = 'spamsp';
print(S.find('am'));
S1 = S.replace('sp','XYz');
print(S1);

line ='a,b,c,f';
line1 = line.split(',');
print(line1);

print(S.upper() + '  '+str(S.isalpha()));

line2 = 'adada  ';
line3 = line2.rstrip();
print("rstrip|"+ line3+"|rstrip");

# 元组操作
print('%s effs, and as %s' % ('spam', 'SPAM'));

print('{0} effs, and as {1}'.format('1spam', '1SPAM'));
