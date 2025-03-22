# Escreva uma função que recebe uma string e retorna um dicionário onde as chaves são os
# caracteres da string e os valores representam quantas vezes cada caractere aparece.

# Exemplo: [‘Java’, ‘Java’, ‘Ruby’, ‘Javascript’, ‘Ruby’]
# Saída: {‘Java’: 2, ‘Ruby’: 2, ‘Javascript’: 1}

def contador(palavras):
    total_contagens = {}
    
    for palavra in palavras:
        if palavra in total_contagens:
            total_contagens[palavra] += 1
        else:
            total_contagens[palavra] = 1
    
    return total_contagens

palavras = ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby', 'Ruby','Ruby']
resultado = contador(palavras)
print(resultado)