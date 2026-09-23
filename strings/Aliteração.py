# -*- coding: utf-8 -*-
import sys

for linha in sys.stdin:
    palavras = linha.split()
    
    contador = 0
    letra_anterior = None
    contou = False
    for palavra in palavras:
        primeira_letra = palavra[0].lower()
        
        if letra_anterior is not None:
            if primeira_letra == letra_anterior and not contou:
                contador += 1
                contou = True
            elif primeira_letra != letra_anterior:
                contou = False
        letra_anterior = primeira_letra
    print(f"{contador}")