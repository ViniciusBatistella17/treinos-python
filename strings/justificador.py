# -*- coding: utf-8 -*-
sequencia = True

while True:

    N = int(input())
    
    if N == 0:
        break
    
    if not sequencia:
        print()
        
    palavras = []
    for i in range(N):
        palavra = input()
        palavras.append(palavra)
    maior_palavra = max(palavras, key=len)
    len(maior_palavra)
    
    for palavra in palavras:
        print(palavra.rjust(len(maior_palavra)))
    


    sequencia = False