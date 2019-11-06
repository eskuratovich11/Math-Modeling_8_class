import numpy as np
import matplotlib.pyplot as plt
def parapola_giperbola(a=1, b=1, c=0, k=1, title='parapola and giperbola'):
    x=np.arange(-10,10,0.01)
    y=a*x**2+b*x+c
    plt.plot(x,y,label='parabola')
    plt.legend()
    x=np.arange(0.01,10,0.01)
    y=k/x
    plt.plot(x,y,label='giperbola')
    plt.show()
parapola_giperbola(a=1, b=1, c=0, k=1, title='parapola and giperbola')