import numpy as np
import matplotlib.pyplot as plt
G=6.672*10**(-11)
R=696000000
c=299792458
M=2*10**30
a=(4*G*M)/(R*c**2)
def circle(R=696000000000000, t=np.arange(-2*np.pi,2*np.pi,0.1)):
    x=R*np.sin(t)
    y=R*np.cos(t)
    plt.plot(x,y, color='k')
    plt.plot([R,R], [-5*R,5*R], color='y')
    plt.plot([R,R*(1-5*np.tan(a))], [0,5*R], color='g')
    plt.axis('equal')
    plt.show()
circle(R=696000000, t=np.arange(-2*np.pi,2*np.pi,0.1))