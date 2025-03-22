# Crie uma função que recebe uma string e conta quantas vezes cada palavra aparece nela.
# Retorne um dicionário onde a chave é a palavra e o valor é a quantidade de ocorrências

# Exemplo: ["banana maçã banana laranja maçã maçã"]
# Saída: {"banana": 2, "maçã": 3, "laranja": 1}

def cont_palavras(palavras):
    total_contagens = {}
    # Para cada palavra na lista de palavras
    for palavra in palavras:
        # Se a palavra já estiver no dicionário, incrementa o valor
        # Se não, cria a chave com o valor 1
        if palavra in total_contagens:
            total_contagens[palavra] += 1
        else:
            total_contagens[palavra] = 1
    # Retorna o dicionário
    return total_contagens

print(cont_palavras(["banana", "maçã", "banana", "laranja", "maçã", "maçã"]))   