import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax=plt.subplots()
tochka, =plt.plot([],[],'o')
x,y=[],[]
edge=6
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def prim_move(t,k,b):
    x=t/t+6.5
    y=t+b
    return x,y
def animate(i):
    tochka.set_data(prim_move(t=i,k=3,b=-8))
ani=FuncAnimation(fig,animate,frames=np.arange(-2*np.pi, 7*np.pi, 0.1),interval=30)
t=np.arange(-2*np.pi,7*np.pi, 0.1)
k=3
b=-8
x=t/t+6.5
y=t+b
plt.plot(x,y, color='y')
plt.axis('equal')
import numpy as np                                    #импортируем библиотеки 
import matplotlib.pyplot as plt
G1=6.6743
G2=10**-11
G=G1*G2 #гравитационная постоянная (м3/кг*с**2)
c1=2.99792458
c2=10**8
c=c1*c2 #скорость света(м/сек)
R1_sun=6.9655
R2_sun=10**8
R_sun=R1_sun*R2_sun #радиус Солнца, м
M1_sun=1.9855
M2_sun=10**30
M_sun=M1_sun*M2_sun #масса Солнца, кг
sdvig_sun=0.5 #расстояние от звезды до луча света х10**8, м
alpha1_sun=(4*G1*M1_sun)/((R1_sun+sdvig_sun)*c1**2)
alpha2_sun=(G2*M2_sun)/(R2_sun*c2**2)
alpha_sun=alpha1_sun*alpha2_sun#угол отклонения, рад
print(alpha_sun,alpha_sun*60*180/3.1415926,alpha_sun*3600*180/3.1415926 )
r0_sun=R1_sun+sdvig_sun #расстояние от центра звезды до луча света
def iskr_sun(R1_sun=6.9655, t=np.arange(-2*np.pi,2*np.pi,0.1)):#Функция созданиия искревленного луча
    x=R1_sun*np.sin(t)
    y=R1_sun*np.cos(t)#параметрическое задание круга
    plt.plot(x,y, color='k')##вызов круга
    plt.plot([r0_sun,r0_sun], [-2*R1_sun,0], color='b')#команда изображения y от x
    plt.plot([r0_sun,r0_sun], [0,2*R1_sun], color='b', linestyle='--')#команда изображения y от x
    plt.plot([r0_sun,r0_sun-2*R1_sun*np.tan(alpha_sun)], [0,2*R1_sun], color='g')#команда изображения y от x
    plt.xlabel('Расстояние*10**8,м') #подпись оси Ох
    plt.ylabel('Расстояние*10**8,м') #подпись оси Оу
    plt.title('Угол отклонения света вблизи Солнца,') #подпись всего графика
    plt.legend() #вызов окна подписей графиков
    plt.axis('equal')
    plt.show()   #команда вывода графика на экран
iskr_sun(R1_sun=6.9655, t=np.arange(-2*np.pi,2*np.pi,0.1))#Вызов функции
plt.show()
ani.save('prin2.gif')