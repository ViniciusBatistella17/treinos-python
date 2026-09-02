while True:
    
    A, B = map(int,input().split())
    
    if A == 0 and B == 0:
        break
    else:
        cartas_A = map(int,input().split())
        cartas_B = map(int,input().split())

        
        conjunto_A = set(cartas_A)
        conjunto_B = set(cartas_B)
        
        diferenca_A = conjunto_A.difference(conjunto_B)
        diferenca_B = conjunto_B.difference(conjunto_A)
        
        quantidade_A = len(diferenca_A)
        quantidade_B = len(diferenca_B)
        
        menor = min(quantidade_A, quantidade_B)
        
        print(f"{menor}")