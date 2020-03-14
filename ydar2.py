import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation
minuta=60
sec_y=365*24*60*60
sec_d=24*60*60
years=1
t=np.arange(0,sec_y,sec_d)

def move_func(s,t):
    
     (x_a, v_x_a, y_a, v_y_a,
      x_b, v_x_b, y_b, v_y_b, 
      x_c, v_x_c, y_c, v_y_c ) = s
     dxdt_a= v_x_a
     dv_xdt_a= (-G*mb* (x_a-x_b)/((x_a-x_b)**2 + (y_a-y_b)**2)**1.5
                -G*mc* (x_a-x_c)/((x_a-x_c)**2 + (y_a-y_c)**2)**1.5)
     dydt_a= v_y_a
     dv_ydt_a=( -G*mb* (y_a-y_b)/((x_a-x_b)**2 + (y_a-y_b)**2)**1.5
                 -G*mc* (y_a-y_c)/((x_a-x_c)**2 + (y_a-y_c)**2)**1.5)
                
     dxdt_b= v_x_b
     dv_xdt_b= (-G*ma* (x_b-x_a)/((x_b-x_a)**2 + (y_b-y_a)**2)**1.5
                -G*mc* (x_b-x_c)/((x_b-x_c)**2 + (y_b-y_c)**2)**1.5)
     dydt_b= v_y_b
     dv_ydt_b= (-G*ma* (y_b-y_a)/((x_b-x_a)**2 + (y_b-y_a)**2)**1.5
                -G*mc* (y_b-y_c)/((x_b-x_c)**2 + (y_b-y_c)**2)**1.5)
     
     dxdt_c= v_x_c
     dv_xdt_c= (-G*ma* (x_c-x_a)/((x_c-x_a)**2 + (y_c-y_a)**2)**1.5
                -G*mb* (x_c-x_b)/((x_c-x_b)**2 + (y_c-y_b)**2)**1.5)
     dydt_c= v_y_c
     dv_ydt_c= (-G*ma* (y_c-y_a)/((x_c-x_a)**2 + (y_c-y_a)**2)**1.5
                -G*mb* (y_c-y_b)/((x_c-x_b)**2 + (y_c-y_b)**2)**1.5)
     
    
     return(dxdt_a, dv_xdt_a, dydt_a, dv_ydt_a,
            dxdt_b, dv_xdt_b, dydt_b, dv_ydt_b,
            dxdt_c, dv_xdt_c, dydt_c, dv_ydt_c)
     
ma=5972*10**24
mb=7.26*10**22
mc=4867*10**24

G=6.67*10**(-11)


x_a0=0
v_x_a0=0
y_a0=0
v_y_a0=0

x_b0=384.4*10**6
v_x_b0=0
y_b0=0
v_y_b0=0

x_c0=-300*10**4
v_x_c0=0
y_c0=0
v_y_c0=0


radius_a= 6371*10**3
radius_b=1737*10**3
radius_c=6051*10**3


s0= (x_a0, v_x_a0, y_a0,v_y_a0,
     x_b0, v_x_b0, y_b0, v_y_b0, 
     x_c0, v_x_c0, y_c0, v_y_c0)  

move_array=np.ndarray(shape=(len(t), 10))
for i in range(len(t)-1):
    tau= [t[i], t[i+1]]
    
    sol=odeint(move_func, s0, tau)
    
    move_array[i,0]= sol[1,0]
    move_array[i,1]= sol[1,2]
    move_array[i,2]= sol[1,4]
    move_array[i,3]= sol[1,6]
    move_array[i,4]= sol[1,8]
    move_array[i,5]= sol[1,10]

    
    x_a0=sol[1,0]
    v_x_a0=sol[1,1]
    y_a0=sol[1,2]
    v_y_a0=sol[1,3]
    
    x_b0=sol[1,4]
    v_x_b0=sol[1,5]
    y_b0=sol[1,6]
    v_y_b0=sol[1,7]
    
    x_c0=sol[1,8]
    v_x_c0=sol[1,9]
    y_c0=sol[1,10]
    v_y_c0=sol[1,11]
    
    r12= np.sqrt((x_a0-x_b0)**2+(y_a0-y_b0)**2)
    r23= np.sqrt((x_b0-x_c0)**2+(y_b0-y_c0)**2)
    r13= np.sqrt((x_c0-x_a0)**2+(y_c0-y_a0)**2)
    
    if r12 <= radius_a+radius_b:
        Vx_a0=(2*mb*v_x_b0+v_x_a0*(ma-mb) )/(ma+mb)
        Vx_b0=(2*ma*v_x_a0+v_x_b0*(mb-ma) )/(ma+mb)
        Vx_c0=v_x_c0
    elif r23 <= radius_b+radius_c:
        Vx_b0=(2*mc*v_x_c0+v_x_b0*(mb-mc) )/(mb+mc)
        Vx_c0=(2*mb*v_x_b0+v_x_c0*(mc-mb) )/(mb+mc)
        Vx_a0=v_x_a0
    elif r13 <= radius_c+radius_a:
        Vx_c0=(2*ma*v_x_a0+v_x_c0*(mc-ma) )/(mc+ma)
        Vx_a0=(2*mc*v_x_c0+v_x_a0*(ma-mc) )/(mc+ma)
        Vx_b0=v_x_b0
    else:
        Vx_a0=v_x_a0
        Vx_b0=v_x_b0
        Vx_c0=v_x_c0
    s0= (x_a0, Vx_a0, y_a0,v_y_a0,
        x_b0, Vx_b0, y_b0, v_y_b0, 
        x_c0, Vx_c0, y_c0, v_y_c0,)  

fig=plt.figure()
planets=[]  

for i in range(0, len(t)-1, 1):
    earth, = plt.plot(move_array[i,0], move_array[i, 1], 'bo', ms=10)
    
    moon,= plt.plot(move_array[i,2], move_array[i, 3], 'o', color='grey', ms=5 )
    
    venera, = plt.plot (move_array[i,4], move_array[i, 5], 'o', color='maroon', ms=10 )
    
    planets.append([earth, moon, venera])
ani = ArtistAnimation(fig, planets, interval= 50)
plt.axis('equal')
ani.save('earth_moon_ven.gif')
    