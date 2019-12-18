import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint


def skorost_func(v, r):
    dvdr=G*m_earth/(r**2*v)
    return dvdr
v_0=0.1
m_earth=5.972*10**24 
r= np.arange(6.4*10**6+10**4, 6.4*10**6,-100)
G=6.67*10**(-11)
solve= odeint(skorost_func, v_0, r)

plt.plot(r, solve[:,0])
plt.show()