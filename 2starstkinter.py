import tkinter as tk
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation
from PIL import Image, ImageTk  

def func():
        m_star = float(entry_1.get())
        v_x_star0 = float(entry_2.get())
        x_star0 = float(entry_3.get())
        sec_y=365*24*60*60
        sec_d=24*60*60
        years=1
        t=np.arange(0,years*sec_y,sec_d)

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

        G=6.67*10**(-11)


        x_sun0=0
        v_x_sun0=10**3
        y_sun0=0
        v_y_sun0=0



        y_star0=0
        v_y_star0=0


        s0= (x_sun0, v_x_sun0, y_sun0,v_y_sun0,
             x_star0, v_x_star0, y_star0, v_y_star0)  
  
        sol=odeint(grav_func, s0, t)

        fig=plt.figure()
        planets=[]  

        for i in range(0, len(t), 1):
            sun, = plt.plot(sol[:i,0], sol[:i, 2], 'y-')
            sun_line, = plt.plot(sol[i,0], sol[i, 2], 'yo')
    
            star,= plt.plot(sol[:i,4], sol[:i, 6], 'r-' )
            star_line, = plt.plot(sol[i,4], sol[i, 6],'ro' )
    
        planets.append([sun, sun_line, star, star_line ])
        ani = ArtistAnimation(fig, planets, interval= 50)
        plt.axis('equal')
        ani.save('2stars.gif')
        image = Image.open('2stars.gif')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(image=photo)
        label.image = photo 
        label.grid(column=0, row=5)
        
root = tk.Tk()
entry_1 = tk.Entry(root)
entry_2 = tk.Entry(root)
entry_3 = tk.Entry(root)
entry_1.grid(column=1, row=0)
entry_2.grid(column=1, row=1)
entry_3.grid(column=1, row=2)

label1 = tk.Label(root, text="масса")
label1.grid(column=0, row=0)

label2 = tk.Label(root, text="скорость")
label2.grid(column=0, row=1)

label2 = tk.Label(root, text="расстояние до Солнца")
label2.grid(column=0, row=2)

button = tk.Button(root, text='показать результат', command=func)
button.grid(column=0, row=3)
root.mainloop()