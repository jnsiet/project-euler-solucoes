"""
>> Sequência Collatz mais Longa

A seguinte sequência iterativa é definida para o conjunto de inteiros positivos:

        n → n/2 (n é par)
        n → 3n + 1 (n é ímpar)

Usando a regra acima e começando com 13, geramos a seguinte sequência:

                    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Pode-se ver que esta sequência (começando em 13 e terminando em 1) contém 10 termos. Embora ainda não tenha
sido provado (Problema de Collatz), pensa-se que todos os números terminam em 1.

Qual número, abaixo de um milhão, produz a sequência mais longa?

NOTA: Assim que a sequência for iniciada, os termos poderão ultrapassar um milhão.
"""

tam_sequencia, maior_sequencia, numero_maior_sequencia = 1, 0, 0

for numero_inicial in range(13, 1_000_000):
    numero = numero_inicial

    while numero != 1:
        if numero % 2 == 0:
            numero /= 2
            tam_sequencia += 1
        else:
            numero = numero * 3 + 1
            tam_sequencia += 1

    if tam_sequencia > maior_sequencia:
        maior_sequencia = tam_sequencia
        numero_maior_sequencia = numero_inicial

    tam_sequencia = 1

print(f"RESPOSTA: {numero_maior_sequencia}")
