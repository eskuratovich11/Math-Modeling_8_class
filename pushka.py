import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 25, 0.1)
def dif(z, t):
    r, v= z
    drdt=v
    dvdt=-(m**2*G*M)/(r**2)
    return drdt, dvdt
M=6*10**24
G=6.67*10**(-11)
m=2
r0 = 6371000
v0 = 50
z0 = r0,v0
solve = odeint(dif, z0, t)
plt.plot(t, solve[:,0])

plt.show()
