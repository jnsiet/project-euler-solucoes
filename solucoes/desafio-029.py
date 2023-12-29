"""
>> Poderes Distintos

Considere todas as combinações inteiras de a^b para 2 ≤ a ≤ 5 e 2 ≤ b ≤ 5:

            2^2 = 4,    2^3 = 8,    2^4 = 16,   2^5 = 32
            3^2 = 9,    3^3 = 27,   3^4 = 81,   3^5 = 243
            4^2 = 16,   4^3 = 64,   4^4 = 256,  4^5 = 1024
            5^2 = 25,   5^3 = 125,  5^4 = 625,  5^5 = 3125

Se eles forem colocados em ordem numérica, com quaisquer repetições removidas, obteremos a seguinte sequência de 15
termos distintos:

            4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125.

Quantos termos distintos existem na sequência gerada por a^b para 2 ≤ a ≤ 100 e 2 ≤ b ≤ 100?
"""

numeros = []

for base in range(2, 101):
    for expoente in range(2, 101):
        potencia = pow(base, expoente)
        if potencia not in numeros:
            numeros.append(potencia)

print(f"RESPOSTA: {len(numeros)}")
