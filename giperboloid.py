import numpy as np 
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d.axes3d as p3

fig=plt.figure()
ax= p3.Axes3D(fig)

a=2
b=3
c=5

phi=np.linspace (0, 2*np.pi, 100)
t= np.linspace(0, np.pi, 100)

x= a* np.outer(np.cos(phi), np.sinh(t))
y= b* np.outer(np.sin(phi), np.sinh(t))
z= c* np.outer(np.ones(np.size(phi)), np.sinh(t))


ax.plot_surface(x,y,z, color='r')

plt.show()