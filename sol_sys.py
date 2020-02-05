import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation
sec_y=365*24*60*60
sec_d=24*60*60
years=10
t=np.arange(0,years*sec_y,sec_d*10)

def grav_func(z,t):
     x_mars, v_x_mars, y_mars, v_y_mars,x_ven, v_x_ven, y_ven, v_y_ven, x_saturn, v_x_saturn, y_saturn, v_y_saturn,x_yup, v_x_yup, y_yup, v_y_yup= z
     dxdt_mars= v_x_mars
     dv_xdt_mars= -G*sun_mass* x_mars/(x_mars**2+y_mars**2)**1.5
     dydt_mars= v_y_mars
     dv_ydt_mars= -G*sun_mass* y_mars/(x_mars**2+y_mars**2)**1.5
     
     dxdt_ven= v_x_ven
     dv_xdt_ven= -G*sun_mass* x_ven/(x_ven**2+y_ven**2)**1.5
     dydt_ven= v_y_ven
     dv_ydt_ven= -G*sun_mass* y_ven/(x_ven**2+y_ven**2)**1.5
     
     dxdt_saturn= v_x_saturn
     dv_xdt_saturn= -G*sun_mass* x_saturn/(x_saturn**2+y_saturn**2)**1.5
     dydt_saturn= v_y_saturn
     dv_ydt_saturn= -G*sun_mass* y_saturn/(x_saturn**2+y_saturn**2)**1.5
     
     dxdt_yup= v_x_yup
     dv_xdt_yup= -G*sun_mass* x_yup/(x_yup**2+y_yup**2)**1.5
     dydt_yup= v_y_yup
     dv_ydt_yup= -G*sun_mass* y_yup/(x_yup**2+y_yup**2)**1.5
     


     return(dxdt_mars, dv_xdt_mars, dydt_mars, dv_ydt_mars, dxdt_ven, dv_xdt_ven, dydt_ven, 
            dv_ydt_ven,dxdt_saturn,dv_xdt_saturn, dydt_saturn, dv_ydt_saturn,
            dxdt_yup,dv_xdt_yup,dydt_yup, dv_ydt_yup )
x0_mars= 0
v_x0_mars=24100
y0_mars=-228*10**9
v_y0_mars=0

x0_ven=-108*10**9
v_x0_ven=0
y0_ven=0
v_y0_ven=-35000

x0_saturn=0
v_x0_saturn=-9690
y0_saturn=1430*10**9
v_y0_saturn=0

x0_yup=0
v_x0_yup=-13070
y0_yup=778.57*10**9
v_y0_yup=0

z0=(x0_mars,v_x0_mars,y0_mars, v_y0_mars, x0_ven,v_x0_ven, y0_ven,v_y0_ven,
    x0_saturn, v_x0_saturn,y0_saturn,v_y0_saturn, x0_yup, v_x0_yup, y0_yup, v_y0_yup)

G=6.67*10**(-11)
sun_mass=1.9*10**30
sol=odeint(grav_func, z0, t)

fig=plt.figure()
planets=[]

for i in range(0, len(t), 1):
    sun, =plt.plot([0], [0], 'yo', ms=10)
    mars, = plt.plot(sol[:i,0], sol[:i, 2], 'r-')
    mars_line, = plt.plot(sol[i,0], sol[i, 2], 'ro')
    
    ven,= plt.plot(sol[:i,4], sol[:i, 6], '-', color= 'maroon' )
    ven_line, = plt.plot(sol[i,4], sol[i, 6],'o', color= 'maroon')
    
    saturn,= plt.plot(sol[:i,8], sol[:i, 10],  '-', color= 'wheat')
    saturn_line, = plt.plot(sol[i,8], sol[i, 10], 'o', color='wheat')
    
    yup,= plt.plot(sol[:i,12], sol[:i, 14], '-', color='goldenrod')
    yup_line, = plt.plot(sol[i,12], sol[i, 14], 'o', color='goldenrod')
    
    planets.append([sun, mars, mars_line, ven, ven_line,saturn,saturn_line, yup, yup_line ])
ani = ArtistAnimation(fig, planets, interval= 50)
plt.axis('equal')
ani.save('solarsys.gif')