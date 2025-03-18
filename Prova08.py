#Criar um dicionario que armazene nome, telefone e email

dic_contato = {}
print("Criando um dicionario com Python")

#solicite ao usuario nome, telefone e email

dic_contato['nome'] = input("Digite seu nome: ")
dic_contato['telefone'] = input("Digite seu telefone: ")
dic_contato['email'] = input("Digite seu email: ")

#Exibindo conteudo do dicionario
print(f"Nome: {dic_contato['nome']}")
print(f"Telefone para contato: {dic_contato['telefone']}")
print(f"Email: {dic_contato['email']}")

