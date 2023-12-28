"""
>> Múltiplos de 3 ou 5

Se listarmos todos os números naturais abaixo 10 que são múltiplos de 3 ou 5, temos 3, 5, 6 e 9. A soma desses
múltiplos é 23.

Encontre a soma de todos os múltiplos de 3 ou 5 abaixo de 1000.
"""

resultado = 0

for multiplo_tres in range(3, 1000, 3):
    resultado += multiplo_tres

for multiplo_cinco in range(5, 1000, 5):
    if multiplo_cinco % 3 == 0:
        continue
    resultado += multiplo_cinco

print(f"RESPOSTA: {resultado}")
