########################################
# Unidad 2                             #
# Metodo de Newton                     #
# Ofelia Cepeda Camargo                #
########################################

import math

def f(x):
    f = x - math.exp(-x)
#    f = x - math.sqrt(3)
    return f

def Df(x):
    df = 1 + math.exp(-x)
#    df = 1
    return df

x = 0.0
n = 0
x1 = 1
while abs(x-x1)>1e-10:
    n = n + 1
    x1 = x
    x = x - (f(x))/(Df(x))

print('La raiz es ', x)
print('Me tomo ', n, 'pasos encontrarla')
    
