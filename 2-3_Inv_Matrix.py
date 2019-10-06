########################################
# 2-3 Matriz inversa                   #
# Este programa calcula la matriz      #
# inversa usando el meetodo de Newton  #
#                                      #
# Autor: Ofelia Cepeda Camargo         #
########################################

import numpy as np

# Se define la matriz a la que le queremos encontrar
# inversa.

A = np.array([[2,5,6,8],[-7,5,6,4],[-1,2,3,5],[0,2,8,9]])

# Este bucle sobre m genera 10 matrices iniciales aleatorias
for m in range (1,11):

    X = np.random.rand(4,4)
    
    # El siguiente bucle es el metodo iterativo para encontrar
    # a la matriz inversa.
    
    for n in range (1,11):
        B = np.identity(4) - A.dot(X)
        X = X + X.dot(B)

    print(X) #Se imprimen las matrices inversas.

