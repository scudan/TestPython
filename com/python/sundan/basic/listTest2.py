import sys

f = open(sys.argv[1])
lines = f.readline()
f.close()

fvaluses = [float(line) for line in lines]

print("min"+min(fvaluses));
print("max"+max(fvaluses));