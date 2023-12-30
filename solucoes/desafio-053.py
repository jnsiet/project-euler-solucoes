"""
>> Seleções Combinatórias

Existem exatamente dez maneiras de selecionar três entre cinco, 12345:

                123, 124, 125, 134, 135, 145, 234, 235, 245 e 345

Em combinatória, usamos a notação, C(5,3) = 10.

Em geral, C(n,r) = n!/r!(n-r)!, onde r ≤ n, n! = n × (n - 1) × ... × 3 × 2 × 1, e 0! = 1.

Somente quando n = 23, é que o valor ultrapassa um milhão: C(23,10) = 1144066.

Quantos valores, não necessariamente distintos, de C(n,r) para 1 ≤ n ≤ 100, são maiores que um milhão?
"""

from math import factorial

contador = 0

for n in range(23, 101):
    for r in range(1, n+1):
        resultado = factorial(n) / (factorial(r) * factorial(n - r))
        if resultado > 1_000_000:
            contador += 1

print(f"RESPOSTA: {contador}")
