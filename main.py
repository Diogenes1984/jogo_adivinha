calendario = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31]
]

lista1 = [
    1, 3, 5, 7,
    9, 11, 13, 15,
    17, 19, 21, 23,
    25, 27, 29, 31
]

lista2 = [
    [2, 3, 6, 7],
    [10, 11, 14, 15],
    [18, 19, 22, 23],
    [26, 27, 30, 31]
]

lista3 = [
    [4, 5, 6, 7],
    [12, 13, 14, 15],
    [20, 21, 22, 23],
    [28, 29, 30, 31]
]

lista4 = [
    [8, 9, 10, 11],
    [12, 13, 14, 15],
    [24, 25, 26, 27],
    [28, 29, 30, 31]
]

lista5 = [
    [16, 17, 18, 19],
    [20, 21, 22, 23],
    [24, 25, 26, 27],
    [28, 29, 30, 31]
]
# ----------------------------------

lista_objetos = [
    'MELANCIA', 'DONALD', 'INFINITO', 'MORANGO', 'PEIXE', 'STOP',
    'RECICLAVEL', 'CEBOLINHA', 'MEG', 'HOMER', 'LISA', 'IN-YANG',
    'CHICO-BENTO', 'BANANA', 'BICILETA', 'BIDU', 'CAVANDO', 'PUFF',
    'BRASIL', 'BART', 'MAÇA', 'PAZ', 'SALSICHA', 'BORBOLETA',
    'RADIO', 'PLUTO', 'NO-SMOKIN', 'TALHERES', 'SIMBA', 'PI', 'MÔNICA'
]

lista_objetos_impressao = [
    ['MELANCIA', 'DONALD', 'INFINITO', 'MORANGO', 'PEIXE', 'STOP'],
    ['RECICLAVEL', 'CEBOLINHA', 'MEG', 'HOMER', 'LISA', 'IN-YANG'],
    ['CHICO-BENTO', 'BANANA', 'BICILETA', 'BIDU', 'CAVANDO', 'PUFF'],
    ['BRASIL', 'BART', 'MAÇA', 'PAZ', 'SALSICHA', 'BORBOLETA'],
    ['RADIO', 'PLUTO', 'NO-SMOKIN', 'TALHERES', 'SIMBA', 'PI', 'MÔNICA'],
]

lista_objetos1 = [
    ['BIDU', 'CAVANDO', 'PUFF', 'BRASIL]'],
    ['BART', 'MAÇA', 'PAZ', 'SALSICHA'],
    ['BORBOLETA', 'RADIO', 'PLUTO', 'NO-SMOKIN'],
    ['TALHERES', 'SIMBA', 'PI', 'MÔNICA'],
]

lista_objetos2 = [
    ['CEBOLINHA', 'MEG', 'HOMER', 'LISA'],
    ['IN-YANG', 'CHICO-BENTO', 'BANANA', 'BICILETA'],
    ['BORBOLETA', 'RADIO', 'PLUTO', 'NO-SMOKIN'],
    ['TALHERES', 'SIMBA', 'PI', 'MÔNICA'],
]

lista_objetos3 = [
    ['MORANGO', 'PEIXE', 'STOP', 'RECICLAVEL'],
    ['IN-YANG', 'CHICO-BENTO', 'BANANA', 'BICILETA'],
    ['BART', 'MAÇA', 'PAZ', 'SALSICHA'],
    ['TALHERES', 'SIMBA', 'PI', 'MÔNICA'],
]

lista_objetos4 = [
    ['DONALD', 'INFINITO', 'STOP', 'RECICLAVEL'],
    ['HOMER', 'LISA', 'BANANA', 'BICILETA'],
    ['PUFF', 'BRASIL', 'PAZ', 'SALSICHA'],
    ['PLUTO', 'NO-SMOKIN', 'PI', 'MÔNICA'],
]

lista_objetos5 = [
    ['MELANCIA', 'INFINITO', 'PEIXE', 'RECICLAVEL'],
    ['MEG', 'LISA', 'CHICO-BENTO', 'BICICLETA'],
    ['CAVANDO', 'BRASIL', 'MAÇA', 'SALSICHA'],
    ['RADIO', 'NO-SMOKIN', 'SIMBA', 'MÔNICA'],
]

BASE1 = 1
BASE2 = 2
BASE4 = 4
BASE8 = 8
BASE16 = 16


def imprime_adivinha(lista, base):
    print("#"*70)
    for item in lista:
        print(item)

    print("#"*70)
    print("")

    resposta = input("O dia do seu aniversário aparece la lista S/N: ")

    if resposta == 's' or resposta == 'S':
        return base
    else:
        base = 0
        return base


def imprime_lista(lista, base):

    resposta = input("A palavra aparece la lista S/N\n")

    if resposta == 's':
        contagem = lista.index(item)
    else:
        contagem = 0

    return contagem


print("#"*70)
for item in lista_objetos_impressao:
    print(item)

print("#"*70)
print("")
escolha = input(
    f"Escolha uma palavra! Quando estiver pronto digite S/n para continuar ou cancelar: ")

if (escolha == 's' or escolha == 'S'):
    contagem = 0
    contagem += imprime_adivinha(lista_objetos1, BASE16)
    contagem += imprime_adivinha(lista_objetos2, BASE8)
    contagem += imprime_adivinha(lista_objetos3, BASE4)
    contagem += imprime_adivinha(lista_objetos4, BASE2)
    contagem += imprime_adivinha(lista_objetos5, BASE1)
else:
    pass


print("#"*70)
print(f"Sua palavra escolhida foi: {lista_objetos[contagem - 1]}")

print("#"*70)
print("")
