import numpy as np
from const import g
x0=1
y0=10
v0=5
t=np.arange(0,5,0.01)

n = len(t)

massiv=np.ndarray(shape=(n,3))


for i in range(0,n,1):
    x=x0+v0*t[i]
    y=y0+v0*t[i]-(g*t[i]**2)/2
    massiv[i,0]=t[i]
    massiv[i,1]=x
    massiv[i,2]=y
    
print(massiv)