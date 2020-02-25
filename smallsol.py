import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation

sec_y=365*24*60*60
sec_d=24*60*60
years=3
t=np.arange(0,years*sec_y,sec_d*2)

def grav_func(z,t):
     (x_mars, v_x_mars, y_mars, v_y_mars,
      x_ven, v_x_ven, y_ven, v_y_ven,
      x_merc, v_x_merc, y_merc, v_y_merc,
      x_earth, v_x_earth, y_earth, v_y_earth)= z
     dxdt_mars= v_x_mars
     dv_xdt_mars= -G*sun_mass* x_mars/(x_mars**2+y_mars**2)**1.5
     dydt_mars= v_y_mars
     dv_ydt_mars= -G*sun_mass* y_mars/(x_mars**2+y_mars**2)**1.5
     
     dxdt_ven= v_x_ven
     dv_xdt_ven= -G*sun_mass* x_ven/(x_ven**2+y_ven**2)**1.5
     dydt_ven= v_y_ven
     dv_ydt_ven= -G*sun_mass* y_ven/(x_ven**2+y_ven**2)**1.5
     
     dxdt_merc= v_x_merc
     dv_xdt_merc= -G*sun_mass* x_merc/(x_merc**2+y_merc**2)**1.5
     dydt_merc= v_y_merc
     dv_ydt_merc= -G*sun_mass* y_merc/(x_merc**2+y_merc**2)**1.5
         
     dxdt_earth= v_x_earth
     dv_xdt_earth= -G*sun_mass* x_earth/(x_earth**2+y_earth**2)**1.5
     dydt_earth= v_y_earth
     dv_ydt_earth= -G*sun_mass* y_earth/(x_earth**2+y_earth**2)**1.5  
     
     return(dxdt_mars, dv_xdt_mars, dydt_mars, dv_ydt_mars, 
            dxdt_ven, dv_xdt_ven, dydt_ven, dv_ydt_ven,
             dxdt_merc, dv_xdt_merc, dydt_merc, dv_ydt_merc,
             dxdt_earth, dv_xdt_earth, dydt_earth, dv_ydt_earth )
x0_mars= 0
v_x0_mars=24100
y0_mars=-228*10**9
v_y0_mars=0

x0_ven=-108*10**9
v_x0_ven=0
y0_ven=0
v_y0_ven=-35000


x0_merc=58*10**9
v_x0_merc=0
y0_merc=0
v_y0_merc=48000

x0_earth=-150*10**9
v_x0_earth=0 
y0_earth=0
v_y0_earth=-30000




z0=(x0_mars,v_x0_mars,y0_mars, v_y0_mars, 
    x0_ven,v_x0_ven, y0_ven,v_y0_ven,
    x0_merc, v_x0_merc, y0_merc, v_y0_merc,
    x0_earth, v_x0_earth, y0_earth, v_y0_earth)

G=6.67*10**(-11)
sun_mass=1.9*10**30
sol=odeint(grav_func, z0, t)

fig=plt.figure()
planets=[]

for i in range(0, len(t), 1):
    sun, =plt.plot([0], [0], 'yo', ms=30)
    
    mars, = plt.plot(sol[:i,0], sol[:i, 2], '-', color='orangered')
    mars_line, = plt.plot(sol[i,0], sol[i, 2], 'o', color='orangered')
    
    ven,= plt.plot(sol[:i,4], sol[:i, 6], '-', color= 'maroon' )
    ven_line, = plt.plot(sol[i,4], sol[i, 6],'o', color= 'maroon')
    
    merc,= plt.plot(sol[:i,8], sol[:i, 10], '-', color='goldenrod')
    merc_line, = plt.plot(sol[i,8], sol[i, 10], 'o', color='goldenrod')
    
    earth,= plt.plot(sol[:i,12], sol[:i, 14], '-', color='lightseagreen')
    earth_line, = plt.plot(sol[i,12], sol[i, 14], 'o', color='lightseagreen')

    planets.append([sun, mars, mars_line, 
                    ven, ven_line,
                    merc, merc_line,
                    earth,earth_line])
ani = ArtistAnimation(fig, planets, interval= 50)
plt.axis('equal')
ani.save('smallsolarsys.gif')