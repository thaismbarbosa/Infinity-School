#ciar um programa em Python para calcular a soma dos números pares dentro 
# de um intervalo determinado pelo usuário. O programa deve solicitar ao 
# usuário que insira dois números inteiros, representando o 
# início e o fim do intervalo (inclusive). 
#Utilize um loop 'for' para iterar sobre todos os números no intervalo e
#somar apenas os números pares. Implemente a estrutura 'else' para exibir
#  uma mensagem indicando que não há números pares no intervalo, caso seja o caso.
#Ao final, exiba a soma dos números pares encontrados.

start = int(input("Digite um número para iniciar: "))
end = int(input("Digite um número para finalizar: "))

#acumuldor de pares
soma_pares = 0

#indentificar se há números pares
pares = False


for i in range(start, end + 1):
    if i % 2 == 0:
        soma_pares += i
        pares = True

if pares:
    print(f"A soma dos pares  {start} a {end} é: {soma_pares}")

else:
    print("Não há pares!")

