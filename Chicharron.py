#########################################
# Programa que calcula las raices de un #
# polinomio de segundo grado.           #
#					#
# Ofelia Cepeda Camargo                 #
#########################################

import math

def Chicharron(a,b,c):
	#Se define el determinante
	Det = b*b - 4*a*c
	#Se evalua si las sol. son reales
	if Det >= 0.0:
        # Se usa la formula gral para encontrar
        # las raices.
		x1 = (-b + math.sqrt(Det))/(2*a)
		x2 = (-b - math.sqrt(Det))/(2*a)
		print('x1=',x1,'; x2=',x2)
	else:
		print('Soluciones complejas')

e1 = 1e10
e2 = 1e-10 

Chicharron(1,-(e1+e2),1)



