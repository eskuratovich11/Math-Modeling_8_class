import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
fig, ax=plt.subplots()
tochka, =plt.plot([],[],'o', ms=10)
tochka2, =plt.plot([],[],'o', ms=10)
x,y=[],[]
x2,y2=[],[]
edge=10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


y0 = 0
v1 = 1

def prim_move2(t,k,b):
     if y2==y:
        x=1
        y=k*t+b
        y2= y0 + t * v1
        x2=1
        y2=y
        return x2, y2, x, y
    else:
        x=1
        y=k*t+b
        y2= y0 + t * v1
        x2=1

        return x2, y2,x, y

def animate(i):
    tochka.set_data(prim_move(t=i,k=1,b=-5))
    tochka2.set_data(prim_move2(t=i))
ani=FuncAnimation(fig,animate,frames=np.arange(0,5,0.1),interval=30)
plt.axis('equal')

ani.save('prin_tochka.gif')