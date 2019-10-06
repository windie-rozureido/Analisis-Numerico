########################################
# 2-3-b                                #
# Matriz inversa condicion inicial     #
# dada                                 #
# Autor: Ofelia Cepeda Camargo         #
########################################

import numpy as np

#Matriz de interes
A = np.array([[2,5,6,8],[-7,5,6,4],[-1,2,3,5],[0,2,8,9]])

#Punto inicial de la iteracion; muy especifico.

X = np.transpose(A)/(22*26)

#A continuacion el algoritmo iterativo

for n in range (1,11):
  B = np.identity(4) - A.dot(X) 
  X = X + X.dot(B)
  
  
print(X)
