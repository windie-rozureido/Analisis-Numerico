#########################################
# Programa para evaluar la derivada de  #
# el seno en un punto.                  #
# Ofelia Cepeda Camargo                 #
#########################################

import math
import matplotlib.pyplot as plt
import numpy as np

#La sig. func. estima la derivada del seno.
#usando diferencia hacia adelante.
def Dsin(x, h):
    derivate = (math.sin(x+h)-math.sin(x))/h
    return derivate

#La sig. func. calcula la derivada del seno
# usando diferencia centrada.

h = np.zeros(15)
error = np.zeros(15)

for i in range(0,15):
    h[i] = 10**(-i) #Se define la 'h' del paso
    x = math.pi/4 #Se define el pnto donde se deriva
    aprox = Dsin(x, h[i]) #Se calcula la aprox primer metodo
    real = math.cos(x) #Este es el valor real
    error[i] = abs((aprox-real))/real #Se calcula el error relatvo

fig, ax = plt.subplots()

ax.set_yscale('log')
ax.semilogx(h, error)
ax.grid()
ax
plt.xlabel('h')
plt.ylabel('error')


plt.show()
