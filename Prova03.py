#CRIE UM JOGO DE ADIVINHAÇÃO

numero_secreto = 7
palpite = None
tentativas = 0
tentativas_maximas = 3

while tentativas < tentativas_maximas:
    palpite = int(input("Tente advinhar o número secreto (entre 1 e 10):"))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns você acertou!")
        break

    elif tentativas < tentativas_maximas:
        print(f"Você errou! Você ainda tem {tentativas_maximas - tentativas} tentativas.")

    else:
        print("Você não conseguiu advinhar o número secreto")

   
