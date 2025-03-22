# Escreva uma função que recebe uma string e retorna um dicionário onde as chaves são os
# caracteres da string e os valores representam quantas vezes cada caractere aparece.

# Exemplo: [‘Java’, ‘Java’, ‘Ruby’, ‘Javascript’, ‘Ruby’]
# Saída: {‘Java’: 2, ‘Ruby’: 2, ‘Javascript’: 1}

# Definir a função contador que recebe uma lista de palavras
def contador(palavras):
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
# Definir a lista de palavras
palavras = ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby', 'Ruby','Ruby']
resultado = contador(palavras) # Chamar a função contador com a lista de palavras
print(resultado)