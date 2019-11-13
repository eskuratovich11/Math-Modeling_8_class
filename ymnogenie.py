import numpy as np
def massiv(a=np.arange(1, 15, 1)):
    b=len(a)
    chislo=1
    for i in range(0, b, 1):
        chislo=chislo*a[i]
    print(chislo)     
massiv(a=np.arange(1, 5, 1))