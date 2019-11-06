import matplotlib.pyplot as plt
from constmodule import c_water, massa_ocean
def armagedon(ma=2345678,va=123456789087654):
    Q=(ma*va**2)/2
    t=Q/c_water*massa_ocean
    if t>=50:
        print('все умрут')
    elif t<50 and t>=50:
        print('почти все умрут')
    elif t<30:   
        print('больно')
    plt.plot(ma,va)
    plt.show()
armagedon(ma=2345678,va=123456789087654)