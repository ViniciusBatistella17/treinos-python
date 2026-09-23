# -*- coding: utf-8 -*-
while True:
    B, N = map(int,input().split())
    
    if B == 0 and N == 0:
        break
    
    reservas = list(map(int,input().split()))
    
    for i in range(N):
        D, C, V = map(int, input().split())
        
        reservas[D - 1] -= V
        reservas[C - 1] += V
    
    marcador = 0
    for reserva in reservas:
        if reserva < 0:
            marcador += 1
    if marcador > 0:
        print("N")
    else:
        print("S")
