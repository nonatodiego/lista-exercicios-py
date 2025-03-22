# Ordenação de Tuplas

# Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade,
# escreva uma função que retorne a lista ordenada pela idade de forma crescente

clubes = [('Vasco da Gama', 126), ('Chelsea', 120), ('Barcelona', 125), ('Inter de Milão', 117)]


def ordenar_idades(lista_idades):
    n = len(lista_idades)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_idades[j][1] > lista_idades[j+1][1]:
             lista_idades[j], lista_idades[j + 1] = lista_idades[j + 1], lista_idades[j]



ordenar_idades(clubes)
print("Lista ordenada pela idade dos clubes: ")
print(clubes)
            