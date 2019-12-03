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
    y=t
    x=b+6*k/(k*k+y*y)
    return x,y
def animate(i):
    tochka.set_data(prim_move(t=i,k=5,b=26.5))
ani=FuncAnimation(fig,animate,frames=np.arange(-6,6,0.1),interval=30)
t=np.arange(-6,6, 0.1)
k=5
b=26.5
y=t
x=b+6*k/(k*k+y*y)
plt.plot(x,y, color='k')
plt.axis('equal')

G1=6.6743
G2=10**-11
G=G1*G2 #гравитационная постоянная (м3/кг*с**2)
c1=2.99792458
c2=10**8
c=c1*c2 #скорость света(м/сек)
R1_neitr_star=2
R2_neitr_star=10**4
R_neitr_star=R1_neitr_star*R2_neitr_star #м
M1_neitr_star=2.464
M2_neitr_star=10**31
M_neitr_star=M1_neitr_star*M2_neitr_star #кг
sdvig_neitr_star=25 #расстояние от звезды до луча света х10**4, м
alpha1_neitr_star=(4*G1*M1_neitr_star)/((R1_neitr_star+sdvig_neitr_star)*c1**2)
alpha2_neitr_star=(G2*M2_neitr_star)/(R2_neitr_star*c2**2)
alpha_neitr_star=alpha1_neitr_star*alpha2_neitr_star #угол отклонения, рад
r0_neitr_star=R1_neitr_star+sdvig_neitr_star #расстояние от центра звезды до луча света
def iskr_neitr_star(R1_neitr_star=2, t=np.arange(-2*np.pi,2*np.pi,0.1)):#Функция созданиия искревленного луча
    x=R1_neitr_star*np.sin(t)
    y=R1_neitr_star*np.cos(t)#параметрическое задание круга
    plt.plot(x,y, color='k')#вызов круга
    plt.plot([27,28.5], [-6,6.5], color='c',linestyle='--')#команда изображения y от x
    plt.xlabel('Расстояние*10**4,м') #подпись оси Ох
    plt.ylabel('Расстояние*10**4,м') #подпись оси Оу
    plt.title('Угол отклонения света вблизи SGR 1806-20') #подпись всего графика
    plt.legend() #вызов окна подписей графиков 
    plt.axis('equal')
    plt.show() #команда вывода графика на экран
iskr_neitr_star(R1_neitr_star=2, t=np.arange(-2*np.pi,2*np.pi,0.1))#Вызов функции
ani.save('prinSGR.gif')