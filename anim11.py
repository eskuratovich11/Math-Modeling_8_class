import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax=plt.subplots()
tochka, =plt.plot([],[],'o')
x,y=[],[]
def cikloida_move(t,R):
    x=R*(t-np.sin(t))
    y=R*(1-np.cos(t))
    return x,y
edge=20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def animate(i):
    tochka.set_data(cikloida_move(t=i,R=2))
    
ani=FuncAnimation(fig,animate,frames=np.arange(-2*np.pi, 4*np.pi, 0.1),interval=30)

t=np.arange(-2*np.pi,4*np.pi, 0.1)
R=2
x=R*(t-np.sin(t))
y=R*(1-np.cos(t))
plt.plot(x,y,color='g')
plt.axis('equal')
ani.save('animate_cikloida.gif')
