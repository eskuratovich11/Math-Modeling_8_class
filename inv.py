import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
t= np.arange(0,15,0.01)
def inv_func(money, t):
    dmdt=-k*money*t
    return dmdt
money_0=1000
k=0.08
solve= odeint(inv_func, money_0, t)
plt.plot(t, solve[:,0])
plt.plot([1], [950], color='b' , marker='o', ms=5)
plt.plot([2], [850], color='b' , marker='o', ms=5)
plt.plot([3], [710], color='b' , marker='o', ms=5)
plt.plot([4], [515], color='b' , marker='o', ms=5)
print(money_0+950+850+710+515)
plt.show()

