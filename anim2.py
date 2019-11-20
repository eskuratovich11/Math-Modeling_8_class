import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax=plt.subplots()
tochka, =plt.plot([],[],'o')
x,y=[],[]
def astroida_move(t=np.arange(-2*np.pi,2*np.pi, 0.1),R=23):
    x=R*np.cos(t)**3
    y=R*np.sin(t)**3
    return x,y
edge=20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def animate (i):
    tochka.set_data(astroida_move(t=np.arange(-2*np.pi,2*np.pi, 0.1),R=23))
ani=FuncAnimation(fig,animate,frames=1000,interval=300)
t=np.arange(-2*np.pi,2*np.pi, 0.1)
R=23
x=R*np.cos(t)**3
y=R*np.sin(t)**3
plt.plot(x,y,color='g',linestyle='--',linewidth=100)
plt.axis('equal')
ani.save('animate_cikloida.gif')

