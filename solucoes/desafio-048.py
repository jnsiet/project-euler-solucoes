"""
>> Poderes Próprios

A série de potências, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Encontre os últimos dez dígitos da série, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

soma = 0

for numero in range(1, 1001):
    soma += pow(numero, numero)

print(f"RESPOSTA: {str(soma)[-10:]}")
