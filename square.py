import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation
a=0.008


t=np.arange(10**(-7),1.5*10**(-7),10**(-9))

def electr_func(s,t):
     
     (xa, v_x_a, ya, v_y_a,
     xb, v_x_b, yb, v_y_b, 
     xc, v_x_c, yc, v_y_c,
     xd, v_x_d, yd, v_y_d) = s
      
     dxdt_a= v_x_a
     dv_xdt_a= (k*qa*qb/ma*(xa-xb)/ ((xa-xb)**2+(ya-yb)**2)**1.5
                +k*qa*qc/ma*(xa-xc)/ ((xa-xc)**2+(ya-yc)**2)**1.5
                +k*qa*qd/ma*(xa-xd)/ ((xa-xd)**2+(ya-yd)**2)**1.5)
     dydt_a= v_y_a
     dv_ydt_a= (k*qa*qb/ma*(ya-yb)/ ((xa-xb)**2+(ya-yb)**2)**1.5
                +k*qa*qc/ma*(ya-yc)/ ((xa-xc)**2+(ya-yc)**2)**1.5
                +k*qa*qd/ma*(ya-yd)/ ((xa-xd)**2+(ya-yd)**2)**1.5)
     
     dxdt_b= v_x_b
     dv_xdt_b= (k*qb*qa/mb*(xb-xa)/ ((xb-xa)**2+(yb-ya)**2)**1.5
                +k*qb*qc/mb*(xb-xc)/ ((xb-xc)**2+(yb-yc)**2)**1.5
                +k*qb*qd/mb*(xb-xd)/ ((xb-xd)**2+(yb-yd)**2)**1.5)
     dydt_b= v_y_b
     dv_ydt_b= (k*qb*qa/mb*(yb-ya)/ ((xb-xa)**2+(yb-ya)**2)**1.5
                +k*qb*qc/mb*(yb-yc)/ ((xb-xc)**2+(yb-yc)**2)**1.5
                +k*qb*qd/mb*(yb-yd)/ ((xb-xd)**2+(yb-yd)**2)**1.5)
    
     dxdt_c= v_x_c
     dv_xdt_c= (k*qc*qa/mc*(xc-xa)/ ((xc-xa)**2+(yc-ya)**2)**1.5
                +k*qc*qb/mc*(xc-xb)/ ((xc-xb)**2+(yc-yb)**2)**1.5
                +k*qc*qd/mc*(xc-xd)/ ((xc-xd)**2+(yc-yd)**2)**1.5)
     dydt_c= v_y_c
     dv_ydt_c= (k*qc*qa/mc*(yc-ya)/ ((xc-xa)**2+(yc-ya)**2)**1.5
                +k*qc*qb/mc*(yc-yb)/ ((xc-xb)**2+(yc-yb)**2)**1.5
                +k*qc*qd/mc*(xc-xd)/ ((xc-xd)**2+(yc-yd)**2)**1.5)
     
     dxdt_d= v_x_d
     dv_xdt_d= (k*qd*qa/md*(xd-xa)/ ((xd-xa)**2+(yd-ya)**2)**1.5
                +k*qd*qb/md*(xd-xb)/ ((xd-xb)**2+(yd-yb)**2)**1.5
                +k*qd*qc/md*(xd-xc)/ ((xd-xc)**2+(yd-yc)**2)**1.5)
     dydt_d= v_y_d
     dv_ydt_d= (k*qd*qa/md*(yd-ya)/ ((xd-xa)**2+(yd-ya)**2)**1.5
                +k*qd*qb/md*(yd-yb)/ ((xd-xb)**2+(yd-yb)**2)**1.5
                 +k*qd*qc/md*(yd-yc)/ ((xd-xc)**2+(yd-yc)**2)**1.5)
     
     return(dxdt_a, dv_xdt_a, dydt_a, dv_ydt_a,
            dxdt_b, dv_xdt_b, dydt_b, dv_ydt_b,
            dxdt_c, dv_xdt_c, dydt_c, dv_ydt_c,
            dxdt_d, dv_xdt_d, dydt_d, dv_ydt_d)

qa= 5.1*10**(-14)
qb= 5.1*10**(-14)
qc= -5.1*10**(-14)
qd= -5.1*10**(-14)

ma=1.1*10**(-27)
mb=1.1*10**(-27)
mc=1.1*10**(-27)
md=1.1*10**(-27)

va=1*10**6
vb=1*10**6
vc=1*10**6
vd=1*10**6

xa0=-a
v_xa0=-va/np.sqrt(2)
ya0=a
v_ya0=-va/np.sqrt(2)

xb0= -a
v_xb0=vb/np.sqrt(2)
yb0=-a
v_yb0=-vb/np.sqrt(2)

xc0= a
v_xc0=-vc/np.sqrt(2)
yc0=a
v_yc0=vc/np.sqrt(2)

xd0= a
v_xd0=vd/np.sqrt(2)
yd0=-a
v_yd0=vd/np.sqrt(2)

k=8.98755*10**9

s0= (xa0, v_xa0, ya0,v_ya0,
     xb0, v_xb0, yb0,v_yb0,
     xc0, v_xc0, yc0,v_yc0,
     xd0, v_xd0, yd0,v_yd0)  
  
sol=odeint(electr_func, s0, t)

fig=plt.figure()
objects=[]  
for i in range(0, len(t), 1):
    a, = plt.plot(sol[:i,0], sol[:i, 2], 'r-')
    a_line, = plt.plot(sol[i,0], sol[i, 2], 'ro')
    
    b,= plt.plot(sol[:i,4], sol[:i, 6], '-', color= 'maroon' )
    b_line, = plt.plot(sol[i,4], sol[i, 6],'o', color= 'maroon')
    
    c,= plt.plot(sol[:i,8], sol[:i, 10],  '-', color= 'y')
    c_line, = plt.plot(sol[i,8], sol[i, 10], 'o', color='y')
    
    d,= plt.plot(sol[:i,12], sol[:i, 14],  '-', color= 'k')
    d_line, = plt.plot(sol[i,12], sol[i, 14], 'o', color='k')

    objects.append([a, a_line, b, b_line, c, c_line, d, d_line ])
ani = ArtistAnimation(fig, objects, interval= 50)
plt.axis('equal')
ani.save('square.gif')