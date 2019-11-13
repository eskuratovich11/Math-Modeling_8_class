def visokosnyu_god(god=2019):
    """
    Эта функция определяет високосный год или нет по заданному значению года.
    """
    b=god%4
    a=god%400
    c=god%100
    if b!=0 or(c==0 and a!=0) :
        print('невисокосный')
    else:
        print('високосный')


visokosnyu_god(2100)