from const import g
def energia(m=5,h=10,v=15):
    ep=m*g*h
    ek=(m*v**2)/2
    e=ep+ek
    print(e)
energia(m=5,h=10,v=15)