import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax=plt.subplots()
tochka, =plt.plot([],[],'o')
x,y=[],[]
def astroida_move(t,R):
    x=R*np.cos(t)**3
    y=R*np.sin(t)**3
    return x,y
edge=20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def animate (i):
    tochka.set_data(astroida_move(t=i,R=2))
    
ani=FuncAnimation(fig,animate,frames=np.arange(-2*np.pi, 4*np.pi, 0.1),interval=30)
t=np.arange(-2*np.pi,4*np.pi, 0.1)
R=2
x=R*np.cos(t)**3
y=R*np.sin(t)**3
plt.plot(x,y,color='g',linestyle='--')
plt.axis('equal')
ani.save('animate_asteroida.gif')

