import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
t= np.arange(0,50,0.1)
def bac_func(q, t):
    dqdt=k*q
    return dqdt
q_0=10
k=0.05
solve= odeint(bac_func, q_0, t)
plt.plot(t, solve[:,0])
plt.show()

