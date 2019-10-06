########################################
# 2-4 La Catenaria                     #
# Este programa calcula la longitud de #
# una cuerda atada a dos postes.       #
# Autora: Ofelia Cepeda Camargo        #
########################################

import math

def f(lamb):

    f = lamb*math.cosh(50.0/lamb)-lamb-23.0
    return f

def Df(lamb):

    df = math.cosh(50.0/lamb)-(50.0/lamb)*math.sinh(50.0/lamb)-1.0
    return df

def Dist(lamb):
    d = 2.0*lamb*math.sinh(50.0/lamb)
    return d

lamb = 55.0

for n in range(1,11):

    lamb = lamb - (f(lamb))/(Df(lamb))

print("El valor de lambda es ",lamb)

d = Dist(lamb)

print("El largo del cable es ", d)


