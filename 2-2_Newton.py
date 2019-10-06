########################################
# Unidad 2 Problema 2b                 #
# Metodo de Newton                     #
# Ofelia Cepeda Camargo                #
########################################

import math


def f(x):
    f = x-math.sqrt(3)
    return f

# Se definen valores iniciales
n = 0
x = 1

# Aqui comienza el metodo de Newton

while abs(x-x1) > 1e-10:
    n = n +  1
    x = x - f(x) #La derivada para esta funcion vale 1.

print('El metodo de Newton tardo ',n)
print('x =', x)
