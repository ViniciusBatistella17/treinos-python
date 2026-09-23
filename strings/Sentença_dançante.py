# -*- coding: utf-8 -*-

import sys

for linha in sys.stdin:
    linha = linha.rstrip("\n")
    proxima_maiuscula = True
    
    frase = ""
    
    for caractere in linha:
        if caractere.isspace():
            frase += caractere
            continue
        else:
            if proxima_maiuscula == True:
                letra = caractere.upper()
            else:
                letra = caractere.lower()
                
        frase += letra
        proxima_maiuscula = not proxima_maiuscula
        
    print(f"{frase}")