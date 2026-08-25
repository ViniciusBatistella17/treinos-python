# -*- coding: utf-8 -*-

T = int(input())

horas = T // 3600
restante = T % 3600

minutos = restante // 60
restante = restante % 60

segundos = restante

print(f"{horas}:{minutos}:{segundos}")