first_name = "David";
last_name ="wang";
phone = "1111111";
stock = ('good',100,490.10);
address = ('www.google.com',80);
person =(first_name,last_name,phone);
filename = "person.txt";
persons = [];
for line in open(filename):
    fields = line.split(",")
    first_name1 = filename[0]
    last_name1 = fields[1]
    phone1 = fields[2]
    person1 =(first_name1,last_name1,phone1);
    persons.append(person1)

for first_name1, last_name1 , phone1 in persons:
    print(last_name1);
#print(person[2]);