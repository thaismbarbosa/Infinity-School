# Criando um codigo simples que use o módulo os para ter acesso ao
# Sistema Operacional e criar uma lista contendo todos os intens!

# Importar o módulo os que é usado para interagir com o Sistema Operacional
import os

# Usado para listar itens no diretório
listas = os.listdir()

print("Arquivos e pastas do diretório: ")

# Usando o for para percorrer os itens na listas
for lista in listas:
    print(lista)