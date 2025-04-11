equipes = [
    ("Brazil", [8.9, 6.7, 9.9]),
    ("Estados Unidos", [10.0, 9.9, 8.8]),
    ("Espanha", [4.4, 6.8, 9.1]),
]

for pais, notas in equipes:
    media = sum(notas) / len(notas)
    print(f"{pais}: média {round(media, 2)}")



    
    
