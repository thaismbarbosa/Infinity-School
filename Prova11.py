
#Criar uma função chamada maior_numeroCrie uma função chamada maior_numero
#que receberá três números como argumentos. 
# Esta função deve comparar os três números e identificar qual deles é o maior. 
# Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois.
#  A função deve então retornar o maior número encontrado

#Criando uma função e usando a estrutura if, elif e else para realizar a comparação
def maior_numero(a, b, c):
    if a >= b and a>= c:
        return a
    elif b >= a and b>= c:
        return b
    else : 
        return c
print(maior_numero(2, 4, 6))   

# Usando a função max(), para simplificar o código!
def maior_numero(a, b, c):
    return max(a, b, c)

print(maior_numero(2, 4, 6))  