########################################
# UNIDAD 2                             #
# Metodo secante                       #
# Ofelia Cepeda Camargo                #
########################################

import math

def f(x):
    f = x-math.exp(-x)
    return f

x = 0.0
y = 1.0
z = 0.5
n = 0
while abs(f(z))>1e-8:
    n = n + 1
    m = (y-x)/(f(y)-f(x))
    z = y - m*f(y)
    x = y
    y = z

print('La raiz es ', z)
print('me tomo ',n,'pasos encontrarla')
    
