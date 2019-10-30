from math import sqrt, pi
from const import k, e, const_planka
t=200
E=300
n= (2/(sqrt(pi)))*(const_planka/(k*t)**(3/2))*(e**(-E/(k*t)))*(E**(t/2))
print(n)