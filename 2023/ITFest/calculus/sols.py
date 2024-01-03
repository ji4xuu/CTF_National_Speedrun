from libnum import n2s
from math import isqrt
from sympy import isprime


with open("output.txt", "r") as f:
    x = int(f.readline())
    z = int(f.readline())
    enc = int(f.readline(), 16)


ab=z-1
a_minus_b = isqrt(x**2-4*ab)
a=(a_minus_b+x)//2
b=ab//a
x_plus_y=a**2+b**2+a+b
a_pangkat3_plus_b_pangkat3=a**3+b**3
val = enc//x_plus_y
print(n2s(val))
print(n2s(a_pangkat3_plus_b_pangkat3))
flag=val^a_pangkat3_plus_b_pangkat3
print(n2s(flag).decode('utf-8')
