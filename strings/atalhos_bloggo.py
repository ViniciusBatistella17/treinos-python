# -*- coding: utf-8 -*-
import sys

for linha in sys.stdin:
    
    frase = ""
    italico = False
    italico_novo = ""
    
    negrito = False
    negrito_novo = ""
    
    linha = linha.rstrip("\n")
    
    for caractere in linha:
        if caractere == "_":
            if italico:
                italico_novo = "</i>"
            else:
                italico_novo = "<i>"
            italico = not italico
        
            frase += italico_novo
        elif caractere == "*":
            if negrito:
                negrito_novo = "</b>"
            else:
                negrito_novo = "<b>"
            negrito = not negrito
            
            frase += negrito_novo
        else:
            frase += caractere
    print(frase)