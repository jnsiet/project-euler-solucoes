"""
>> Pontuações por Nomes

Usando names.txt, um arquivo de texto de 46KB contendo mais de cinco mil nomes, comece classificando-os em
ordem alfabética. Em seguida, calculando o valor alfabético de cada nome, multiplique esse valor pela sua
posição alfabética na lista para obter uma pontuação do nome.

Por exemplo, quando a lista é ordenada em ordem alfabética, COLIN, que vale 3 + 15 + 12 + 9 + 14 = 53, é o
938º nome na lista. Assim, COLIN obteria uma pontuação de 938 × 53 = 49714.

Qual é o total de todas as pontuações de nomes no arquivo?
"""

lista_nomes = []
posicao_nome, pontuacao_nome, pontuacao_total = 1, 0, 0

alfabeto = {"A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,
            "K": 11,
            "L": 12,
            "M": 13,
            "N": 14,
            "O": 15,
            "P": 16,
            "Q": 17,
            "R": 18,
            "S": 19,
            "T": 20,
            "U": 21,
            "V": 22,
            "W": 23,
            "X": 24,
            "Y": 25,
            "Z": 26}

with open("../files/names.txt", "r") as arquivo:
    linha = arquivo.readline()
    for nome in linha.split(","):
        lista_nomes.append(nome.replace('"', ""))

lista_nomes.sort()

for nome in lista_nomes:
    for letra in nome:
        pontuacao_nome += alfabeto[letra]
    pontuacao_total = pontuacao_total + pontuacao_nome * posicao_nome
    pontuacao_nome = 0
    posicao_nome += 1

print(f"RESPOSTA: {pontuacao_total}")
