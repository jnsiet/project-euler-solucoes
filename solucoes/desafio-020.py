"""
>> Soma Fatorial de Dígitos

n! significa n × (n − 1) × ... × 3 × 2 × 1.

Por exemplo, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
e a soma dos dígitos do número 10! é 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Encontre a soma dos dígitos do número 100!.
"""

from math import factorial

numero = factorial(100)
soma_digitos = 0

for digito in str(numero):
    soma_digitos += int(digito)

print(f"RESPOSTA: {soma_digitos}")
