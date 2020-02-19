import numpy as np 
from matplotlib import pyplot as plt 
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation 

fig=plt.figure()
ax= p3.Axes3D(fig)

h1=7
N=100
phi=np.linspace ( 2*np.pi, 0, N)
t= np.linspace(6*np.pi, 0, N)

x=np.outer(phi, np.cos(t))
y=np.outer(phi, np.sin(t))
z=h1*np.outer(np.ones(np.size(phi)), t)


ax.plot_surface(x,y,z, color='y')


x1= phi*np.cos(t)
y1= phi* np.sin(t)
z1= h1*t

ball,=ax.plot(x1,y1,z1,'ro' )


def anim_func(i):

    ball.set_data(x1[i], y1[i])
    ball.set_3d_properties(z1[i])
    
#ax.set_xlim3d([-1.0, 1.0])
#ax.set_xlabel('X')
#
#ax.set_ylim3d([-1.0, 1.0])
#ax.set_ylabel('Y')
#
#ax.set_zlim3d([-1.0, 1.0])
#ax.set_zlabel('Z')
    
ani=animation.FuncAnimation(fig, anim_func, N, interval=50 )    

plt.show()

ani.save('gelikoid2.gif')