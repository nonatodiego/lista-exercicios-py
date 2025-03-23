# Verificador de Palídromo

def palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

print(palindromo("radar"))
print(palindromo("luz azul"))
print(palindromo("python"))
