"""
>> Menor Múltiplo

2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10 sem qualquer resto.

Qual é o menor número positivo que é igualmente divisível por todos os números de 1 a 20?
"""

from itertools import count

encontrou_solucao = False

for dividendo in count(start=2520, step=10):
    for divisor in range(3, 21):
        if dividendo % divisor != 0:
            break
        elif divisor == 20:
            encontrou_solucao = True
    if encontrou_solucao:
        print(f"RESPOSTA: {dividendo}")
        break
