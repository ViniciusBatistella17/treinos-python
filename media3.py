# -*- coding: utf-8 -*-
N1, N2, N3, N4 = map(float, input().split())

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")

elif media < 5.0:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")

elif 5.0 <= media <= 6.9:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    exame = float(input())
    nota = (media + exame) / 2
    print(f"Nota do exame: {exame:.1f}")
    if nota >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {nota:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {nota:.1f}")