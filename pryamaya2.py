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
    x=t/t+9.7
    y=t+b
    return x,y
def animate(i):
    tochka.set_data(prim_move(t=i,k=3,b=-15))
ani=FuncAnimation(fig,animate,frames=np.arange(-2*np.pi, 11*np.pi, 0.1),interval=30)
t=np.arange(-2*np.pi,11*np.pi, 0.1)
k=3
b=-15
x=t/t+9.7
y=t+b
plt.plot(x,y, color='y')
plt.axis('equal')
G1=6.6743
G2=10**-11
G=G1*G2 #гравитационная постоянная (м3/кг*с**2)
c1=2.99792458
c2=10**8
c=c1*c2 #скорость света(м/сек)
R1_VY=9.8789
R2_VY=10**11
R_VY=R1_VY*R2_VY #м
M1_VY=3.384
M2_VY=10**31
M_VY=M1_VY*M2_VY #кг
sdvig_VY=1 #расстояние от звезды до луча света х10**11, м
alpha1_VY=(4*G1*M1_VY)/((R1_VY+sdvig_VY)*c1**2)
alpha2_VY=(G2*M2_VY)/(R2_VY*c2**2)
alpha_VY=alpha1_VY*alpha2_VY #угол отклонения, рад
print(alpha_VY,alpha_VY*60*180/3.1415926,alpha_VY*3600*180/3.1415926 )
r0_VY=R1_VY+sdvig_VY #расстояние от центра звезды до луча света
def iskr_VY(R1_VY=9.8789, t=np.arange(-2*np.pi,2*np.pi,0.1)):#Функция созданиия искревленного луча
    x=R1_VY*np.sin(t)
    y=R1_VY*np.cos(t)#параметрическое задание круга
    plt.plot(x,y, color='k')#вызов круга
    plt.plot([r0_VY,r0_VY], [-2*R1_VY,0], color='y') #команда изображения y от x
    plt.plot([r0_VY,r0_VY], [0,2*R1_VY], color='y', linestyle='--') #команда изображения y от x
    plt.plot([r0_VY,r0_VY-2*R1_VY*np.tan(alpha_VY)], [0,2*R1_VY], color='r') #команда изображения y от x
    plt.xlabel('Расстояние*10**11,м')#подпись оси Ох
    plt.ylabel('Расстояние*10**11,м') #подпись оси Оу
    plt.title('Угол отклонения света вблизи VY Большого пса') #подпись всего графика
    plt.legend() #вызов окна подписей графиков 
    plt.axis('equal')
    plt.show() #команда вывода графика на экран
iskr_VY(R1_VY=9.8789, t=np.arange(-2*np.pi,2*np.pi,0.1))#Вызов функции
plt.show()
ani.save('prinVY.gif') 