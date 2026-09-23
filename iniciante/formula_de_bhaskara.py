# -*- coding: utf-8 -*-
import math

pontoA, pontoB, pontoC = map(float, input().split())

delta = pontoB ** 2 - 4 * pontoA * pontoC

if pontoA == 0 or delta < 0:
    print("Impossivel calcular")
else:
    x1 = (-pontoB + math.sqrt(delta)) / (2 * pontoA)
    x2 = (-pontoB - math.sqrt(delta)) / (2 * pontoA)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
