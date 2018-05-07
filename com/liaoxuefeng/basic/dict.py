d={'M' : 97 , 'B': 75, 'T':85}
print(d['T'])

d['A'] = 47

print(d['A'])

d['J'] = 22
print(d['J'])

print('DD' in d);

#获取不存在的值
print(d.get('Thomas'))
print(d.get('Thomas', -1))


d.pop('T')

print(d)

d.pop('M')
print(d)