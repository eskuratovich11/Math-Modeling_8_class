import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 10, 0.01)
def dif(z, t):
    x, y= z
    dxdt=(a-c*y)*x
    dydt=(-b+delta*x)*y
    return dxdt, dydt
a=1
c=2
b=3
delta=2
x0=5
y0=4
z0 = x0, y0
solve = odeint(dif, z0, t)
plt.plot(solve[:,0], solve[:,1])

plt.show()