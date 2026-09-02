# -*- coding: utf-8 -*-

N = int(input())
coelhos = 0
ratos = 0
sapos = 0

for i in range(N):
    quantidade, caractere = input().split()
    numero_quantidade = int(quantidade)
    if caractere == "C":
        coelhos += numero_quantidade
    if caractere == "R":
        ratos += numero_quantidade
    if caractere == "S":
        sapos += numero_quantidade

total = coelhos + ratos + sapos
percentual_coelho = (coelhos / total) * 100
percentual_ratos = (ratos / total) * 100
percentual_sapos = (sapos /total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_coelho:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %") 