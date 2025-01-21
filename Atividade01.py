#calcular a media anual de um aluno
media = "4"
nota_01 = float(input("Digite a 1º nota do bimestre:"))
nota_02 = float(input("Digite a 2º nota do bimestre:"))
nota_03 = float(input("Digite a 3º nota do bimestre:"))
nota_04 = float(input("Digite a 4º nota do bimestre:"))

soma = (nota_01 + nota_02 + nota_03 + nota_04)
media = (f'A media do aluno é {soma / 4}')

print(media)
