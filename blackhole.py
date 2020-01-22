import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
t= np.arange(0,10**13,10**8)
def dif(m, t):
    dmdt=-h*c**4/(15360*np.pi*G**2*m**2)
    return dmdt
c=3*10**8
h=6.62*10**(-34)
G=6.62*10**(-11)
m0=10**11
solve= odeint(dif, m0, t)
plt.plot(t, solve)
plt.show()