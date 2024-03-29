#########################################
# Programa para evaluar la derivada de  #
# el seno en un punto.                  #
# Ofelia Cepeda Camargo                 #
#########################################

import math
import numpy as np
import matplotlib.pyplot as plt

#La sig. func. calcula la derivada del seno
# usando diferencia centrada.

def Dsin2(x,h):
    derivate = (math.sin(x+h)-math.sin(x-h))/(2*h)
    return derivate

h = np.zeros(15)
error = np.zeros(15)

for i in range(0,15):
    h[i] = 10**(-i) #Se define la 'h' del paso
    x = math.pi/4 #Se define el pnto donde se deriva
    aprox = Dsin2(x,h[i]) #Se calcula la aprox segundo metodo
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
