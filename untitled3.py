import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 10, 0.01)
def dif(c, t):
    x, y, z= c
    dxdt=o*y-o*x
    dydt=p*x-x*z-y
    dzdt=x*y-b*z
    return dxdt, dydt, dzdt
o=10
b=5
p=4
x0=5
y0=4
z0=2
c0 = x0, y0, z0
solve = odeint(dif, c0, t)
plt.plot(solve[:,1], solve[:,2])

plt.show()