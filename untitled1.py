import numpy as np                                    #импортируем библиотеки 
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
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
r0_sun=R1_sun+sdvig_sun #расстояние от центра звезды до луча света

fig = plt.figure()
# =============================================================================
# x = np.arange(r0_sun, r0_sun-2*R1_sun*np.tan(alpha_sun) ,0.1)
# y = np.arange(-2*R1_sun,2*R1_sun, 0.1)
# =============================================================================
x1 = np.arange(7.4655, 0, -0.1)
y1 = np.arange(-13.931, 0, 0.1)
x2 = np.arange(7.4655, 0.00011, -0.1)
y2 = np.arange(0, 13.931, 0.1)                

z = []

for i in range(14):
    ball1, = plt.plot(x1[:i], y1[:i], 'o')
    ball2, = plt.plot(x2[:i], y2[:i], 'o')
    
    z.append([ball1, ball2])
ani = ArtistAnimation(fig, z, interval=50)
# =============================================================================
# edge=20
# fig.set_xlim(-edge, edge)
# fig.set_ylim(-edge, edge)
# =============================================================================
plt.axis('equal')
ani.save('dajhf.gif')