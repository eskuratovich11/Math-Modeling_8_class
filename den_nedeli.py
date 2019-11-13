def den_nedeli(chislo=15,mesac=6,god1=1992):
    a=(14-mesac)//12
    god=god1-a
    mesac1=mesac+(12*a)-2
    dennedeli=(chislo+(31*mesac1)//12+god+god//4-god//100+god//400)%7
    if dennedeli==0:
        x='воскресенье'
    elif dennedeli==1:
        x='понедельник'
    elif dennedeli==2:
        x='вторник'
    elif dennedeli==3:
        x='среда'
    elif dennedeli==4:
        x='четверг'
    elif dennedeli==5:
        x='пятница'
    elif dennedeli==6:
        x='суббота'
    print(x)
den_nedeli(chislo=15,mesac=6,god1=1992)    
    
