#Desenvolva um programa em Python para calcular a média de notas 
#de alunos em uma disciplina. O programa deve solicitar ao usuário 
#o número de alunos e, em seguida, para cada aluno, pedir o nome e 
#três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

#Além disso, implemente uma estrutura condicional para verificar 
#se cada aluno foi aprovado ou reprovado, considerando que a média 
#mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a 
#indicação de aprovação ou reprovação.

#Ao final, exiba a média geral da turma.

#definir um número de alunos para realizar o calculo

num_alunos = int(input("Digite o número de alunos: "))
soma_geral = 0

for i in range( 3):
    print(f"\nAluno {i + 1}:")

    nome = input("Digite o nome do Aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3 / 3)
    print(media)

#Verificar se o aluno foi aprovado ou não
if media >= 7.0:
        resultado = "Aprovado"

else:
        print("Reprovado")

#exibir resultado pro aluno
print(f"Nome: {nome}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média: {media: .2f}")
print(f"Situação: {resultado}")     

#calcular media geral

soma_geral += media
media_geral = soma_geral / num_alunos
print(f"\aMédia geral da turma: {media_geral : .2f}")



