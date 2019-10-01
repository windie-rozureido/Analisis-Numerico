########################################
# Unidad 2 Problema 2                  #
# Metodos Iterativos                   #
# Ofelia Cepeda Camargo                #
########################################

import math

def g1(x):
    g = 3 + x - x*x
    return g

def g2(x):
    g = 1 + x - x*x/3
    return g
def f(x):
    f = x-math.sqrt(3)
    return f

x1 = 1
x2 = 1
n = 0

for i in range(1,21):
    n = n + 1
    x1 = g1(x1)
    x2 = g2(x2)
    print(n, x2)

print('Despues de ',n,'pasos:')
#print('g1 regresa x=',x1)
print('g2 devuelve x =',x2)

n = 0

x = 1
x1 = 0
while abs(x-x1) > 1e-10:
    n = n +  1
    x1= x
    x = x - f(x)

print('El metodo de Newton tardo ',n)
print('x =', x)
