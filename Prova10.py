# Crie uma função chamada media que receberá três números como argumentos. 
# Esta função deve calcular a média aritmética desses três números.

#solicitar os numeros aos usuarios
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Criando a função
def media(num1, num2, num3):
    #Somando os numeros
    soma = num1 + num2 + num3
    #Calculando a media
    media_aritmetica = soma / 3
    return media_aritmetica

#Imprimindo o resultado
print(f"A média dos numeros é:" , media (num1, num2, num3)) 