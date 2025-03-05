#Programa de sistema de login

#Definir nome e senha
nome_de_usuario = "admin"
senha_correta = "0102"

#Definir o número de tentativas
tentativas = 3

while tentativas > 0:
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
#Se estiver correto tem que enviar uma mensagem de boas vindas
    if usuario == nome_de_usuario and senha == senha_correta:
        print("Bem-vindo, login realizado com sucesso!")
        break
#Se estiver errado tem que enviar uma mensagem de erro    
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Usuário e senha incorretos. Você tem {tentativas} restantes.")
        else:
            print("Acesso bloqueado, por ultrapassar o número de tentativas!")
#Usar o loop for para enviar uma mensagem de erro repetida 3 vezes!            
            for tentativas in range(3):
                print("Acesso bloqueado!")
                
