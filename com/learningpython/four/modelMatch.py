import re;
#正则表达式
match = re.match('Hello[\t]*(.*)world','Hello   Python  Pythony world')
result = match.groups();
print (result);
match1 = re.match('/(.*)/(.*)/(.*)','/usr/home/lll')
result = match1.groups();
print(result)