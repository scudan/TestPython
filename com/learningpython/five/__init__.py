import decimal
from fractions import Fraction
dec = decimal.Decimal(1) / decimal.Decimal(7)
print(dec);
decimal.getcontext().prec = 4;
dec1 = decimal.Decimal(1) / decimal.Decimal(7)
print(dec1);

x = Fraction(1,3);
print(x)
y = Fraction(1,5);

z = x+y;
print(z);
z1 = x -y;
print(z1)
z2 = x * y;
print(z2);
z3= x / y;
print(z3);

az = x + Fraction(*(4.0/3).as_integer_ratio())
#22517998136852479/13510798882111488
print(az)
#限制数值的大小
azz = az.limit_denominator(10);
#5/3
print(azz)