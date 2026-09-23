# -*- coding: utf-8 -*-
import math 
import sys 

for linha in sys.stdin: 
    R1 ,X1, Y1, R2, X2, Y2 = map(int, linha.split()) 

    distancia =(X2 - X1) ** 2 + (Y2 - Y1) ** 2 
    raiz = math.sqrt(distancia) 
    circulo = raiz + R2 

    if R1 >= circulo: 
        print("RICO") 
    elif R1 < circulo: 
        print("MORTO")
