"""
>> Soma de Dígitos de Potência

2^15 = 32768 e a soma de seus algarismos é 3 + 2 + 7 + 6 + 8 = 26.

Qual é a soma dos algarismos do número 2^1000?
"""

numero = pow(2, 1000)
soma_digitos = 0

for digito in str(numero):
    soma_digitos += int(digito)

print(f"RESPOSTA: {soma_digitos}")
