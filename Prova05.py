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
def calcular_media():
    # Solicita o número de alunos
    num_alunos = int(input("Digite o número de alunos: "))

    soma_geral = 0

    #informações de cada aluno
    for i in range(num_alunos):
        print(f"\nAluno {i + 1}:")
        
        # Solicita o nome e as três notas do aluno
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        # Calcula a média do aluno
        media = (nota1 + nota2 + nota3) / 3
        
        # Verificar situação do aluno
        situacao = "Aprovado" if media >= 7.0 else "Reprovado"
        
        # Exibir o resultado
        print(f"\nNome: {nome}")
        print(f"Notas: {nota1}, {nota2}, {nota3}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        
        #Acumuladora para descobrir a media
        soma_geral += media

    # Calcula e exibe a média geral da turma
    media_geral = soma_geral / num_alunos
    print(f"\nMédia geral da turma: {media_geral:.2f}")


calcular_media()
