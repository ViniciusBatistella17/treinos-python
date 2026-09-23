# -*- coding: utf-8 -*-

A, B, C = map(int, input().split())
 
maiorAB = (A + B + abs(A - B)) // 2

if maiorAB > C:
    print(f"{maiorAB} eh o maior")
else:
    print(f"{C} eh o maior")
