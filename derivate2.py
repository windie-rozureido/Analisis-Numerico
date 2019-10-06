#########################################
# Programa para evaluar la derivada de  #
# el seno en un punto.                  #
# Ofelia Cepeda Camargo                 #
#########################################

import math


#La sig. func. calcula la derivada del seno
# usando diferencia centrada.

def Dsin2(x,h):
    derivate = (math.sin(x+h)-math.sin(x-h))/(2*h)
    return derivate

for i in range(0,15):
    h = 10**(-i) #Se define la 'h' del paso
    x = math.pi/4 #Se define el pnto donde se deriva
    aprox = Dsin2(x,h) #Se calcula la aprox segundo metodo
    real = math.cos(x) #Este es el valor real
    error = (aprox-real)/real #Se calcula el error relatvo


    print(h, aprox, real, error) #Se tabula los resltds
