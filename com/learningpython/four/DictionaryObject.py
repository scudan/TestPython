#字典对象
#不是序列,而是一种映射
D = {'food':'Spam','qua':4,'color':'pink'}
print(D['food'])
print(D['qua']+1)


D1 = {};
D1['name'] ='scudan';
D1['job'] = 'dev';
D1['age'] = 40;
print(D1);

rec ={'job': ['dev','mgr'],
      'age': 40,
      'name': {'first':'scudan','last':'dan'}}

print(rec['name']);
print(rec['name']['last']);
print(rec['job']);
print(rec['job'][0]);
rec['job'].append('test');
print(rec);

D3= {'a':1,'b':2,'c':3}
Ks = list(D3.keys())
print(Ks);

Ks.sort()
print(Ks);
for key in Ks:
    print(key,'=>',D3[key])

if not 'f' in D3:
        print('missing');

value = D3.get('x',2);
print(value);
value = D3['x'] if 'x' in D3 else 33;
print(value);
value = D3['a'] if 'a' in D3 else 34;
print(value);