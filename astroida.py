import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig= plt.figure()
R=8
t=np.linspace(-2*np.pi,2*np.pi,100)

def circle_big(R,t):
    x_b=R*np.cos(t)
    y_b=R*np.sin(t)
    plt.plot(x_b, y_b, color='k')
    return x_b, y_b
circle_big(R,t)

def circle_small(x_centre,y_centre, R, N):
    x=np.zeros(N)
    y=np.zeros(N)
    for i in range(0,N,1):
        x[i]=x_centre+(R/4)*np.cos(t[i])
        y[i]=y_centre+(R/4)*np.sin(t[i])
    return x,y
x_astr=R*np.cos(t)**3
y_astr=R*np.sin(t)**3
anim_list=[]
N=100
x_centre=0.75*R*np.cos(t)
y_centre=0.75*R*np.sin(t)
for i in range(0,N,1):
    x,y = circle_small(x_centre[i],y_centre[i], R, N)
    astroida,= plt.plot(x_astr[:i+1], y_astr[:i+1],'k-', lw=2)
    circle,= plt.plot(x, y, 'b-', lw=2)
    tochka,= plt.plot(x_astr[i], y_astr[i],'ro')
    anim_list.append([astroida, circle, tochka])
ani=ArtistAnimation(fig,anim_list, interval=50)
plt.axis('equal')
ani.save('astroida.gif')