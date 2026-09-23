# -*- coding: utf-8 -*-
teste = int(input()) 

for i in range(teste): 
    frase = input() 
    frase = frase.lower()

    frequencia = {}
    
    for letra in frase: 
        if not letra.isalpha():
            continue
        else:
            frequencia[letra] = frequencia.get(letra, 0) + 1
        
    maior = max(frequencia.values())
    
    repetidas = ""
    
    for letra, quantidade in frequencia.items():
        if quantidade == maior:
            repetidas += letra
    
    resultado = "".join(sorted(repetidas))
    
    print(f"{resultado}")