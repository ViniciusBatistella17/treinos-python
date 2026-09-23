# -*- coding: utf-8 -*-

n1, n2, n3 = map(int, input().split())

lista = [n1, n2, n3]

ordenada = lista.copy()
ordenada.sort()
print(ordenada[0])
print(ordenada[1])
print(ordenada[2])
print()
print(lista[0])
print(lista[1])
print(lista[2])
