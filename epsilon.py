###############################################
# Este programa calcula la unidad de redondeo #
#                                             #
# Ofelia Cepeda Camargo                       #
###############################################

import numpy as np

import math

a = 4/3

b = a - 1

c = b + b + b

u = math.abs(c - 1)

eps = np.finfo(float).eps

error = math.abs(u - eps) / math.abs(eps)

print("El valor calculado para la unidad de redondeo es", u)

print("El valor real es", eps)

print("El error relativo es", error)




