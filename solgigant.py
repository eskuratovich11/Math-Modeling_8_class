import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation
sec_y=365*24*60*60
sec_d=24*60*60
years=30
t=np.arange(0,years*sec_y,sec_d*50)

def grav_func(z,t):
     ( x_saturn, v_x_saturn, y_saturn, v_y_saturn,
      x_yup, v_x_yup, y_yup, v_y_yup,
      x_uran, v_x_uran, y_uran, v_y_uran,
      x_neptun, v_x_neptun, y_neptun, v_y_neptun)= z
     
     dxdt_saturn= v_x_saturn
     dv_xdt_saturn= -G*sun_mass* x_saturn/(x_saturn**2+y_saturn**2)**1.5
     dydt_saturn= v_y_saturn
     dv_ydt_saturn= -G*sun_mass* y_saturn/(x_saturn**2+y_saturn**2)**1.5
     
     dxdt_yup= v_x_yup
     dv_xdt_yup= -G*sun_mass* x_yup/(x_yup**2+y_yup**2)**1.5
     dydt_yup= v_y_yup
     dv_ydt_yup= -G*sun_mass* y_yup/(x_yup**2+y_yup**2)**1.5
     
     dxdt_uran= v_x_uran
     dv_xdt_uran= -G*sun_mass* x_uran/(x_uran**2+y_uran**2)**1.5
     dydt_uran= v_y_uran
     dv_ydt_uran= -G*sun_mass* y_uran/(x_uran**2+y_uran**2)**1.5
     
     dxdt_neptun= v_x_neptun
     dv_xdt_neptun= -G*sun_mass* x_neptun/(x_neptun**2+y_neptun**2)**1.5
     dydt_neptun= v_y_neptun
     dv_ydt_neptun= -G*sun_mass* y_neptun/(x_neptun**2+y_neptun**2)**1.5


     return(dxdt_saturn,dv_xdt_saturn, dydt_saturn, dv_ydt_saturn,
            dxdt_yup,dv_xdt_yup,dydt_yup, dv_ydt_yup,
             dxdt_uran, dv_xdt_uran, dydt_uran, dv_ydt_uran,
             dxdt_neptun, dv_xdt_neptun,dydt_neptun, dv_ydt_neptun )


x0_saturn=0
v_x0_saturn=-9690
y0_saturn=1430*10**9
v_y0_saturn=0

x0_yup=0
v_x0_yup=-13070
y0_yup=778.57*10**9
v_y0_yup=0

x0_uran=0
v_x0_uran=-7000
y0_uran=2875*10**9
v_y0_uran=0

x0_neptun=0
v_x0_neptun=-5000
y0_neptun=4497*10**9
v_y0_neptun=0


z0=(x0_saturn, v_x0_saturn,y0_saturn,v_y0_saturn,
    x0_yup, v_x0_yup, y0_yup, v_y0_yup,
    x0_uran, v_x0_uran, y0_uran, v_y0_uran,
    x0_neptun, v_x0_neptun, y0_neptun, v_y0_neptun )

G=6.67*10**(-11)
sun_mass=1.9*10**30
sol=odeint(grav_func, z0, t)

fig=plt.figure()
planets=[]

for i in range(0, len(t), 1):
    sun, =plt.plot([0], [0], 'yo', ms=10)
    
    saturn,= plt.plot(sol[:i,0], sol[:i, 2],  '-', color= 'wheat')
    saturn_line, = plt.plot(sol[i,0], sol[i, 2], 'o', color='wheat')
    
    yup,= plt.plot(sol[:i, 4], sol[:i, 6], '-', color='burlywood')
    yup_line, = plt.plot(sol[i,4], sol[i, 6], 'o', color='burlywood')
    
    uran,= plt.plot(sol[:i,8], sol[:i, 10], '-', color='deepskyblue')
    uran_line, = plt.plot(sol[i,8], sol[i, 10], 'o', color='deepskyblue')
    
    neptun,= plt.plot(sol[:i,12], sol[:i, 14], '-', color='steelblue')
    neptun_line, = plt.plot(sol[i, 12], sol[i, 14], 'o', color='steelblue')
    
    planets.append([sun,
                    saturn,saturn_line, 
                    yup, yup_line,
                    uran, uran_line,
                    neptun, neptun_line])
ani = ArtistAnimation(fig, planets, interval= 50)
plt.axis('equal')
ani.save('gigant_solarsys.gif')