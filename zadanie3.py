import numpy as np
import matplotlib.pyplot as plt
def circle_ellipse(R=1, title='circle_ellips',a=5,b=6):
    x=np.arange(-2,2,0.1)
    y=np.arange(-2,2,0.1)
    X,Y=np.meshgrid(x,y)
    fxy=X**2+Y**2
    plt.contour(X,Y,fxy,levels=[R])
    x=np.arange(-5,5,0.1)
    y=np.arange(-5,5,0.1)
    X,Y=np.meshgrid(x,y)
    f=X**2/a**2+Y**2/b**2
    plt.contour(X,Y,f,levels=[1])
    plt.legend()
    plt.show()
circle_ellipse(R=1, title='circle_ellips',a=2,b=1)
