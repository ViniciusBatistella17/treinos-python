# -*- coding: utf-8 -*-
N = int(input())

for i in range(N):
    frase = input()
    letras = set()
    for caractere in frase:
        if caractere.isalpha():
            letras.add(caractere)
            
    if len(letras) == 26:
        print("frase completa")
    elif len(letras) >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")