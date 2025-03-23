# Dada uma lista de números, crie uma função que retorne os três números mais frequentes
# em ordem decrescente de frequência. Se houver empates, ordene pelo valor numérico.

def mais_frequentes(numeros):
    # Contar a frequência de cada número
    frequencias = {}
    # Iterar sobre os números
    for numero in numeros:
        # Verificar se o número já está no dicionário
        if numero in frequencias:
            # Se estiver, incrementar a frequência
            frequencias[numero] += 1
        else:
            # Se não estiver, adicionar o número com frequência
            frequencias[numero] = 1
    # Função auxiliar para definir a chave de ordenação
    def chave_ordenacao(numero):
        return (frequencias[numero], -numero)
    # Ordenar os números por frequência
    mais_frequentes = sorted(frequencias.keys(), key=chave_ordenacao, reverse=True)[:3]
    return mais_frequentes

print(mais_frequentes([1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5])) 
