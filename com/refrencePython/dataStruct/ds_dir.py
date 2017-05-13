knights = {'gh':'the pure','robin': 'the brave'}
for k ,v in knights.items():
    print(k,":", v )


for i,v in enumerate(['tic','dac','toe']):
    print(i,v)


questions =['name','quest','fav color']
answers = ['lancelot','the holy grail', 'blue']

for q,a in zip(questions,answers):
    print("what is your {0}? It is {1}.".format(q,a))