########################################
# 2-6 Parabolas                        #
#                                      #
# Autor: Ofelia Cepeda Camargo         #
########################################

import numpy as np

def F(x):
  f = (np.array([x[0]**2 - x[1] - 1, - x[0] + x[1]**2 - 1]))
  return f

def DF(x):
  df = (np.array([[2*x[0], - 1], [- 1, 2 * x[1]]]))
  return df

def Newton(x):
    s = np.array([0.0, 0.0])
    for n in range(1,16):
        A = DF(x)
        B = -1.0*F(x)
        s = np.linalg.solve(A, B)
        x = x + s
    return x

x1 = np.array([-0.61, -0.61])
x2 = np.array([0.1, -1.1])
x3 = np.array([-1.1, 0.1])
x4 = np.array([1.61, 1.61])

x1 = Newton(x1)

x2 = Newton(x2)

x3 = Newton(x3)

x4 = Newton(x4)
  
print("Los puntos de intersección de las parábolas son:")

print("x_1 = ", x1)
print("x_2 = ", x2)
print("x_3 = ", x3)
print("x_4 = ", x4)
  
