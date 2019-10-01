########################################
# Programa para encontrar una raiz en  #
# el intervalo (1,0) de la funcion     #
# f(x) = x-exp(-x)                     #
# Ofelia Cepeda Camargo                #
########################################

import math

# A continuacion se define la funcion

def f(x): 
    f = x - math.exp(-x)
    return f

#En las siguientes lineas se definen
# los puntos iniciales y finales del
# intervalo.

a = 0.0
b = 1.0
xm = (b-a)/2 # Punto medio del intervalo
n = 0  # contador de pasos


#Se entrara al loop si la longitud del intervo
# sea mayor a 10^-8 y abs(f(xm)) > 10^-8

while abs(f(xm))>1e-8 and (b-a)>1e-8:
    n = n + 1
    if  f(a)*f(xm)<0.0:
        # La raiz esta entre a y xm
        # b pasa a ser xm
        b = xm
        xm = a + (b-a)/2
        
        
    else:
        #En otro caso la raiz esta
        #entre xm y b
        # a pasa a ser xm
        a = xm
        xm = a + (b-a)/2
        

#Se imprime el resultado en pantalla.
print('La raiz es ', xm)
print('me tomo ', n, 'pasos llegar a la raiz')
        
