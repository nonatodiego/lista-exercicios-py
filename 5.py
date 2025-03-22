# Dado um dicionário onde as chaves são nomes de alunos e os valores são listas com suas
# notas, crie uma função que retorna uma lista de tuplas, onde cada tupla contém o nome do
# aluno e sua média de notas.

# Exemplo: {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
# Saída: [("Ana", 8.0), ("Bruno", 5.33), ("Carlos", 9.67)]

# Função para calcular a média das notas
def media_notas(notas):
    # Lista para armazenar as médias
    medias = []
    # Para cada aluno e suas notas
    for aluno, notas in notas.items():
        # Calcula a média das notas
        media = sum(notas) / len(notas)
        # Arredonda a média para duas casas decimais
        media = round(media, 2)
        # Adiciona o aluno e sua média na lista de médias
        medias.append((aluno, media))
    return medias   

print(media_notas({"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}))
