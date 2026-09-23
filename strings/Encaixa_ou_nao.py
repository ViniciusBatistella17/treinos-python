# -*- coding: utf-8 -*-
testes = int(input())

for i in range(testes):
    A, B = input().split()
    
    if A[-len(B):] == B:
        print("encaixa")
    else:
        print("nao encaixa")