########################################


import numpy as np

# Definimos la funcion de interes

def F(x):
  f = (np.array([31.4 * x[0]*x[0] - 28.54 * x[0]*x[1] + 65.3 * x[1]*x[1] +
                 365.9*x[0] - 125.7 * x[1] - 22.4, 
                -14.8 * x[1] * x[1] - 92.1 * x[0] + 47.6 * x[1] - 100.3]))
  return f

# Escribimos su correspondiente Jacobiano

def DF(x):
  df = (np.array([[62.8 * x[0] - 28.5 * x[1] + 365.9, -28.54 * x[0] + 
                   130.6 * x[1] - 125.7], 
                  [-92.1,-29.6 * x[1] + 47.6]]))
  return df


# Valores iniciales del algoritmo

x = np.array([100,150.0])
s = np.array([0.0, 0.0])

# El bucle principal

for n in range(1,31):

    A = DF(x)
    B = - 1.0 * F(x)

    s = np.linalg.solve(A, B) # El sistema lineal lo resuelve numpy

    x = x + s
  
print("La colision es en el punto ", x)
  
