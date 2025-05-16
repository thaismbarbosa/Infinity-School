# Criei um codigo bem simples para realizar a função def e importar o módulo random.

import random


# Função lancar_dados
def lancar_dados():
    # Usando o randint para gerar números inteiros de forma aleatória
    dado1 = random.randint(1, 6) 
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    return soma

resultado = lancar_dados()
# Exibir um resultado com a soma de dados gerados aleatoriamente
print("Resultado do lançamento dos dados", resultado) 
