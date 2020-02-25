import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation

sec_y=365*24*60*60
sec_d=24*60*60
years=1
t=np.arange(0,years*sec_y,sec_d)

#sun, mercury, venus, earth, mars, star  
def grav_func(s,t):
    
     (x_sun, v_x_sun, y_sun, v_y_sun,
     x_star, v_x_star, y_star, v_y_star) = s
      
     dxdt_sun= v_x_sun
     dv_xdt_sun= -G*m_star* (x_sun-x_star)/((x_sun-x_star)**2 + (y_sun-y_star)**2)**1.5
     dydt_sun= v_y_sun
     dv_ydt_sun= -G*m_star* (y_sun-y_star)/((x_sun-x_star)**2 + (y_sun-y_star)**2)**1.5

                
     dxdt_star= v_x_star
     dv_xdt_star= -G*m_sun* (x_star-x_sun)/((x_star-x_sun)**2 + (y_star-y_sun)**2)**1.5
     dydt_star= v_y_star
     dv_ydt_star=-G*m_sun* (y_star-y_sun)/((x_star-x_sun)**2 + (y_star-y_sun)**2)**1.5

    
     return(dxdt_sun, dv_xdt_sun, dydt_sun, dv_ydt_sun,
            dxdt_star,dv_xdt_star, dydt_star, dv_ydt_star)
     
m_sun=1.98847*10**30
m_star= 2*10**30
G=6.67*10**(-11)


x_sun0=0
v_x_sun0=10**3
y_sun0=0
v_y_sun0=0

x_star0=-10**3
v_x_star0=10**4
y_star0=0
v_y_star0=0


s0= (x_sun0, v_x_sun0, y_sun0,v_y_sun0,
     x_star0, v_x_star0, y_star0, v_y_star0)  
  
sol=odeint(grav_func, s0, t)

fig=plt.figure()
planets=[]  

for i in range(0, len(t), 1):
    sun, = plt.plot(sol[:i,0], sol[:i, 2], 'k-')
    sun_line, = plt.plot(sol[i,0], sol[i, 2], 'ko')
    
    star,= plt.plot(sol[:i,4], sol[:i, 6], 'r-' )
    star_line, = plt.plot(sol[i,4], sol[i, 6],'ro' )
    
    planets.append([sun, sun_line, star, star_line ])
ani = ArtistAnimation(fig, planets, interval= 50)
plt.axis('equal')
ani.save('21stars.gif')