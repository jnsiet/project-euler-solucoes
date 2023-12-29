"""
>> Número de Fibonacci de 1000 Dígitos

A sequência de Fibonacci é definida pela relação de recorrência:

        F_n = F_{n−1} + F_{n−2}, onde F_1 = 1 e F_2 = 1.

Onde os primeiros 12 termos são:

                            F_1 = 1
                            F_2 = 1
                            F_3 = 2
                            F_4 = 3
                            F_5 = 5
                            F_6 = 8
                            F_7 = 13
                            F_8 = 21
                            F_9 = 34
                            F_10 = 55
                            F_11 = 89
                            F_12 = 144

O 12º termo, F_12, é o primeiro termo a conter três dígitos.
Qual é o índice do primeiro termo na sequência de Fibonacci que contém 1000 dígitos?
"""

ultimo_termo, termo, indice = 0, 1, 1

while len(str(termo)) != 1000:
    aux = ultimo_termo + termo
    ultimo_termo = termo
    termo = aux
    indice += 1

print(f"RESPOSTA: {indice}")
