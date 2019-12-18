import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
t= np.arange(0,100,1)
def skorost_func(v, t):
    dvdt=(F/m)-((Y*v**2)/m)
    return dvdt
v_0=10
F=10
m=10
Y=0.5
solve= odeint(skorost_func, v_0, t)
plt.plot(t, solve[:,0])
plt.show()

