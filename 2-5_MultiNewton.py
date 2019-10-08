########################################
# 2-5 Newton Multidimensional          #
# Este programa encuentra la inter-    #
# sección de dos elipses.              #
# Autora: Ofelia Cepeda Camargo        #
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

x1 = np.array([-1.0,3.0])
s1 = np.array([0.0, 0.0])

x2 = np.array([-10.0,-5.5])
s2 = np.array([0.0, 0.0])

# El bucle principal

for n in range(1,51):

    A1 = DF(x1)
    A2 = DF(x2)
    
    B1 = - 1.0 * F(x1)
    B2 = - 1.0 * F(x2)
    
    s1 = np.linalg.solve(A1, B1) # El sistema lineal lo resuelve numpy
    s2 = np.linalg.solve(A2, B2)
    
    x1 = x1 + s1
    x2 = x2 + s2 
    
print("Posibles puntos de colisión: ")
print("x_1 = ", x1)
print("x_2 = ", x2)
  
