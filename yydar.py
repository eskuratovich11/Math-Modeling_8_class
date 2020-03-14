import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation
sec=60
sec_y=365*24*60*60
sec_d=24*60*60
years=1
t=np.arange(0,sec_d,sec)

def move_func(s,t):
    
     (x_earth, v_x_earth, y_earth, v_y_earth,
     x_moon, v_x_moon, y_moon, v_y_moon) = s
      
     dxdt_earth= v_x_earth
     dv_xdt_earth= -G*m_moon* (x_earth-x_moon)/((x_earth-x_moon)**2 + (y_earth-y_moon)**2)**1.5
     dydt_earth= v_y_earth
     dv_ydt_earth= -G*m_moon* (y_earth-y_moon)/((x_earth-x_moon)**2 + (y_earth-y_moon)**2)**1.5

                
     dxdt_moon= v_x_moon
     dv_xdt_moon= -G*m_earth* (x_moon-x_earth)/((x_moon-x_earth)**2 + (y_moon-y_earth)**2)**1.5
     dydt_moon= v_y_moon
     dv_ydt_moon=-G*m_earth* (y_moon-y_earth)/((x_moon-x_earth)**2 + (y_moon-y_earth)**2)**1.5

    
     return(dxdt_earth, dv_xdt_earth, dydt_earth, dv_ydt_earth,
            dxdt_moon,dv_xdt_moon, dydt_moon, dv_ydt_moon)
     
m_earth=5972*10**24
m_moon=7.26*10**22

G=6.67*10**(-11)


x_earth0=0
v_x_earth0=0
y_earth0=0
v_y_earth0=0

x_moon0=384.4*10**6
v_x_moon0=0
y_moon0=0
v_y_moon0=0

radius_earth= 6371*10**3
radius_moon=1737*10**3
s0= (x_earth0, v_x_earth0, y_earth0,v_y_earth0,
     x_moon0, v_x_moon0, y_moon0, v_y_moon0)  

move_array=np.ndarray(shape=(len(t), 4))
for i in range(len(t)-1):
    tau= [t[i], t[i+1]]
    
    sol=odeint(move_func, s0, tau)
    
    move_array[i,0]= sol[1,0]
    move_array[i,1]= sol[1,2]
    move_array[i,2]= sol[1,4]
    move_array[i,3]= sol[1,6]
    
    x_earth0=sol[1,0]
    v_x_earth0=sol[1,1]
    y_earth0=sol[1,2]
    v_y_earth0=sol[1,3]
    
    x_moon0=sol[1,4]
    v_x_moon0=sol[1,5]
    y_moon0=sol[1,6]
    v_y_moon0=sol[1,7]
    
    r12= np.sqrt((x_earth0-x_moon0)**2+(y_earth0-y_moon0)**2)
    if r12 <= radius_earth+radius_moon:
        Vx_earth0=(2*m_moon*v_x_moon0+v_x_earth0*(m_earth-m_moon) )/(m_earth+m_moon)
        Vx_moon0=(2*m_earth*v_x_earth0+v_x_moon0*(m_moon-m_earth) )/(m_earth+m_moon)
    else:
        Vx_earth0=v_x_earth0
        Vx_moon0=v_x_moon0
    s0= (x_earth0, Vx_earth0, y_earth0,v_y_earth0,
     x_moon0, Vx_moon0, y_moon0, v_y_moon0)  

fig=plt.figure()
planets=[]  

for i in range(0, len(t)-1, 1):
    earth, = plt.plot(move_array[i,0], move_array[i, 1], 'bo', ms=6)
    
    moon,= plt.plot(move_array[i,2], move_array[i, 3], 'o', color='grey', ms=3 )

    
    planets.append([earth, moon])
ani = ArtistAnimation(fig, planets, interval= 50)
plt.axis('equal')
ani.save('earth_moon.gif')
    