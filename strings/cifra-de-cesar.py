# -*- coding: utf-8 -*-
N = int(input())

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(N):
    frase_certa = ""
    frase = input()
    posicao = int(input())
    
    for caractere in frase:
        indice = ord(caractere) - ord("A")
        posicao_certa = (indice - posicao) % 26
        
        frase_certa += chr(posicao_certa + ord("A"))
    print(f"{frase_certa}")