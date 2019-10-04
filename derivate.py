#########################################
# Programa para evaluar la derivada de  #
# el seno en un punto.                  #
# Ofelia Cepeda Camargo                 #
#########################################

import math

#La sig. func. estima la derivada del seno.
#usando diferencia hacia adelante.
def Dsin(x, h):
    derivate = (math.sin(x+h)-math.sin(x))/h
    return derivate

#La sig. func. calcula la derivada del seno
# usando diferencia centrada.



for i in range(0,15):
    h = 10**(-i) #Se define la 'h' del paso
    x = math.pi/4 #Se define el pnto donde se deriva
    aprox = Dsin(x, h) #Se calcula la aprox primer metodo
    real = math.cos(x) #Este es el valor real
    error = (aprox-real)/real #Se calcula el error relatvo


    print(h, aprox, real, error) #Se tabula los resltds
    
