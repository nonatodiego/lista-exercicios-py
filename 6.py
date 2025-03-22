# Escreva uma função que recebe dois dicionários onde as chaves são strings e os valores são
# inteiros. A função deve combinar os dicionários somando os valores das chaves que
# aparecem em ambos.

def soma_dicionarios(d1, d2):
    # Armanezar o resultado da soma dos dicionários
    d3 = {}
    # interar sobre as chaves do primeiro dicionário
    for chave in d1:
        if chave in d2:
            # Se a chave estiver nos dois dicionários, somar os valores
            d3[chave] = d1[chave] + d2[chave]
        else:
            # Copiar o valor se a chave estiver apenas em um dos dicionários
            d3[chave] = d1[chave]
            
    for chave in d2:
        # Copiar o valor se a chave estiver apenas em um dos dicionários
        if chave not in d1:
            d3[chave] = d2[chave]
    return d3

print(soma_dicionarios({"a": 2, "b": 3, "c": 5}, {"a": 1, "b": 4, "d": 7})) 