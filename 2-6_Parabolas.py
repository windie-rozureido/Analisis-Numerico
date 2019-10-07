########################################
# 2-6 Parabolas
#
# Autor: Ofelia Cepeda Camargo


import numpy as np

def F(x):
  f = (np.array([x[0]**2 - x[1] - 1, - x[0] + x[1]**2 - 1]))
  return f

def DF(x):
  df = (np.array([[2*x[0], - 1], [- 1, 2 * x[1]]]))
  return df

x = np.array([1,1.5])
s = np.array([0.0, 0.0])
for n in range(1,16):
  A = DF(x)
  B = -1.0*F(x)
  s = np.linalg.solve(A, B)
  x = x + s
  
print("La colision es en el punto ", x)
  
