"""
>> Múltiplos Permutados

Pode-se ver que o número, 125874, e seu duplo, 251748, contêm os mesmos dígitos, mas em uma ordem diferente.

Encontre o menor número inteiro positivo, x, de tal modo que 2x, 3x, 4x, 5x e 6x, contêm os mesmos dígitos.
"""

from itertools import count

encontrou_solucao = False

for numero in count(start=1):
    for multiplicador in range(2, 6):
        produto_atual_ordenado = ''.join(sorted(str(numero * multiplicador)))
        proximo_produto_ordenado = ''.join(sorted(str(numero * (multiplicador + 1))))

        if produto_atual_ordenado != proximo_produto_ordenado:
            break
        elif multiplicador == 5:
            print(f"RESPOSTA: {numero}")
            encontrou_solucao = True
            break

    if encontrou_solucao:
        break
