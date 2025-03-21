# Primeiro Exercício: Soma de elementos pares

# Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os elementos pares contidos nela.
# Exemplo: [2,4,10,3,9,7,15,22]
# Saída: A soma dos pares é: x

msg = input("Digite uma lista de números inteiros:")

lista_string = msg.split() 

lista_numeros = [int(numero) for numero in lista_string]


def somar_pares(lista_numeros):
    somar_pares = 0

    for numero in lista_numeros:
        if numero % 2 == 0:
            somar_pares += numero

    return somar_pares

resultado = somar_pares(lista_numeros)

print ("A soma dos pares é:", resultado)
        