# -*- coding: utf-8 -*-
N = int(input())

for i in range(N):
    numero = input()
    
    leds = {
        "0": 6,
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6,
    }
   
    total = 0
    for digito in numero:
        total += leds[digito]
    
    
    print(f"{total} leds")
