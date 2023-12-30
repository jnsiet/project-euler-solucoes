"""
>> Números Pares de Fibonacci

Cada novo termo na sequência de Fibonacci é gerado pela adição dos dois termos anteriores. Começando com 1 e 2, 
os primeiros 10 termos são:

						1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Considerando os termos da sequência de Fibonacci cujos valores não excedem quatro milhões, encontre a soma dos
termos que são pares.
"""

from itertools import count

termo, ultimo_termo, soma = 1, 0, 0

for numero in count(start=1):
	aux = ultimo_termo + termo
	ultimo_termo = termo
	termo = aux

	if termo % 2 == 0:
		soma += termo

	elif termo >= 4_000_000:
		break

print(f"RESPOSTA: {soma}")
