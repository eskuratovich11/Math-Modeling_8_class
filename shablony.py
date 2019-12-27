#библиотеки
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from matplotlib.animation import ArtistAnimation
from scipy.integrate import odeint
#цикл
for i in range(a,b,1):
    print(n**i,end=' ')
if:
    oluo
elif:
    hjyfkg
    
else:
    werdhfj
print()

#массив
import numpy as np
from const import g
x0=1
y0=10
v0=5
t=np.arange(0,5,0.01)

n = len(t)

massiv=np.ndarray(shape=(n,3))


for i in range(0,n,1):
    x=x0+v0*t[i]
    y=y0+v0*t[i]-(g*t[i]**2)/2
    massiv[i,0]=t[i]
    massiv[i,1]=x
    massiv[i,2]=y
    
print(massiv)
#функция
def func(m=5,h=10,v=15):

    print(e)
func(m=5,h=10,v=15)
# рисовалка
import matplotlib.pyplot as plt 
plt.plot([3,3], [2,5.5], color='b', marker='.', ms=10, linestyle='--',linewidth=1)
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('cube')
plt.show()
#РИСОВАЛКА ФУНКЦИЕЙ 
import numpy as np
import matplotlib.pyplot as plt
def parapola(a=1, b=1, c=0, k=1, title='parapola '):
    x=np.arange(-10,10,0.01)
    y=a*x**2+b*x+c
    plt.plot(x,y,label='parabola')
    plt.legend()
    plt.show()
parapola_giperbola(a=1, b=1, c=0, k=1, title='parapola')
#АНИМАЦИЯ
  
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
# АНИМАЦИЯ2
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
#дифференциал

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
t= np.arange(0,100,1)
def skorost_func(v, t):
    dvdt=(F/m)-((Y*v**2)/m)
    return dvdt
v_0=10
F=10
m=10
Y=0.5
solve= odeint(skorost_func, v_0, t)
plt.plot(t, solve[:,0])
plt.show()
# dif2
import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0, 5, 0.1)
def dif(z, t):
    s, v= z
    dsdt=v
    dvdt=-g*np.sin(s/l)-k/m*v
    return dsdt, dvdt
l=3
g=9.81
k=2
m=2
s0 = 0
v0 = 2
z0 = s0,v0
solve = odeint(dif, z0, t)
plt.plot(t, solve)

plt.show()