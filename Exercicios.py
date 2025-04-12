i# Atividade 1 (*args)
def concatenar_strings(*args):
    resultado = ""
    for string in args:
        resultado += string
    return resultado
print(concatenar_strings("Thais ", "Desenvolvedora ", "FullStack"))

# Atividade 2 map()

def dobrar(numero):
    return numero * 2
numeros = [1, 2, 3, 4, 5]
resultado = map(dobrar, numeros)
print(list(resultado))

# Atividade 3 filter()

def par(numero):
    return numero % 2 == 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(par, numeros)
print(list(pares))

# Usando a função lambda
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(lambda x: x % 2 == 0,  numeros)
print(list(pares))

# Atividade 4 reduce()

from functools import reduce
def maior_string(lista):
    return reduce(lambda a, b: a if len(a) >= len(b) else b, lista)
strings = ["maçã", "banana", "kiwi", "abacaxi"]
print(maior_string(strings))

# Atividade 5

def criar_lista_de_compras(*args):
    return list(args)

print(criar_lista_de_compras('areia ', 'tijolo ', 'cimento'))

# Atividade 6 lambda

paridade = lambda x: 'par' if x % 2 == 0 else 'impar' 
print(paridade(2))
print(paridade(3))