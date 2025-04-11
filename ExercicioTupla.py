# Criando uma tupla
# A contagem de indices começa em 0

palestrantes = (
    ("Caio Carneiro" , "Como eu faço" , "Vendc"), #[0]
    ("Betina Rudolph", "Imagem é Poder", "Líbertas") , #[1]
    ("Bruno Perini", "Viver de Renda", "Grupo Primo" ),#[2]
         #[0]              [1]              [2]
)

terceiro_paletrante = palestrantes[2]
print(f"Nome: {terceiro_paletrante[0]}")
print(f"Tema da palestra: {terceiro_paletrante[1]}")
print(f"Instituição: {terceiro_paletrante[2]}")


