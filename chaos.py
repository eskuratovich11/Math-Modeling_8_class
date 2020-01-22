import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 200, 0.1)
def dif(z, t):
    x, w= z
    dxdt=w
    dwdt=m*(1-x**2)*w-x
    return dxdt, dwdt
m=0.001
x0=10
w0=15
z0 = x0, w0
solve = odeint(dif, z0, t)
#plt.plot(t, solve)
plt.plot(solve[:,0], solve[:,1])

plt.show()