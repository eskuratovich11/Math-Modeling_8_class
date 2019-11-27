import numpy as np
import matplotlib.pyplot as plt
G=6.6743*10**(-11)
R=np.arange(20000, 10**9, 200000)
c=299792458
M=2.464*10**31
y= lambda x: (4*G*M)/(x*c**2)
fig = plt.subplots()
x=np.linspace(19000, 50000, 1000)
plt.plot(x,y(x),color='y')
plt.show()

M=2*10**30
y= lambda x: (4*G*M)/(x*c**2)
fig = plt.subplots()
x=np.linspace(696000000, 6960000000, 10000)
plt.plot(x,y(x),color='b')
plt.show()

M=3.381*10**31
y= lambda x: (4*G*M)/(x*c**2)
fig = plt.subplots()
x=np.linspace(9.8789*10**11, 9.8789*10**12, 1000000)
plt.plot(x,y(x), color='r')
plt.show()
    
    