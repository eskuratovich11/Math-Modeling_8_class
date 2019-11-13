def kalendar(ostatok=1, olimpiad=75, mesac=7):
    nachalo=-776
    god=nachalo+((olimpiad-1)*4)-ostatok
    a=god+1
    b=god-1
    if mesac>=7:
        print(a)
    else:
        print(b)
kalendar(ostatok=1, olimpiad=75, mesac=7)
