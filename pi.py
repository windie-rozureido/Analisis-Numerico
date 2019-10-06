########################################
# Programa para calcular el perimetro  #
# d poligonos regulares.               #
# Ofelia Cepeda Camargo                #
########################################

import math

def pn1(n):
    p = 2*math.sqrt(2)
    for i in range(3,n+1):
        p = 2**(i-1)*math.sqrt(2*(1-math.sqrt(1-(p/2**(i-1))**2)))
    return p

def pn2(n):
    r = 2/(2+math.sqrt(2))
    p = 4*math.sqrt(r)
    for i in range(4, n+1):
        r = r/(2+math.sqrt(4-r))
        p = 2**(i-1)*math.sqrt(r)
    return p

for n in range(3, 61):
    pn = pn1(n)
    pm = pn2(n)
    print(n, pn, pm)


    
