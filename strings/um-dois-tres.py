# -*- coding: utf-8 -*-
Quantidade = int(input())

palavra_certas = ["one", "two", "three"]

for i in range(Quantidade):
    palavra = input()
    
    for correta in palavra_certas:
        if len(palavra) == len(correta):
            diferentes = 0
        
            for posicao in range(len(palavra)):
                if palavra[posicao] != correta[posicao]:
                    diferentes += 1
                
            if diferentes <= 1:
                indice = palavra_certas.index(correta)
                resultado = indice + 1
                print(resultado)