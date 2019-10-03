#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:35:15 2019

@author: Ofelia Cepeda Camargo
"""
import math
def Chicharronera(a,b,c):
    if a != 0.0: 
        if b*b-4*a*c >= 0:     
            if b < 0.0:
                x1 =  (-b + math.sqrt(b*b - 4*a*c))/(2*a)
                x2 = 2*c/(-b+math.sqrt(b*b - 4*a*c))
            if b > 0.0:
                x1 =  (-b - math.sqrt(b*b - 4*a*c))/(2*a)
                x2 = 2*c/(-b-math.sqrt(b*b - 4*a*c))
        if b*b-4*a*c < 0.0:
            print("Soluciones no reales.")
    if a == 0.0:
        x1 = c/b
        x2 = x1
#    y1 = (2*c)/(-b-math.sqrt(b*b - 4*a*c))
#    y2 = (2*c)/(-b+math.sqrt(b*b - 4*a*c))
    print(x1, x2)
#    print(y1, y2)
    
Chicharronera(0.05010, -98.78, 5.015)

