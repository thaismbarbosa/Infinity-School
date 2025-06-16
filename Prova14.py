#criando a primmeira classe
class Animal:
    def __init__(self):
        pass
        
    def falar(self):
        print('Este animal faz um som genérico.')

meu_animal = Animal()
meu_animal.falar()

#criando a segunda classe 
class Cachorro:
    def __init__(self, raca, nome):
        self.raca = raca
        self.nome = nome

    def falar(self):
        print(f'O cachorro {self.nome} está latindo!')

meu_cachorro = Cachorro("Pastor-Alemão", "Thor")
print(meu_cachorro.raca)
print(meu_cachorro.nome)
meu_cachorro.falar()

#criando a terceira classe
class Gato:
    def __init__(self, raca, nome):
        self.raca = raca
        self.nome = nome

    def falar(self):
            print(f'O gato {self.nome} está miando!')

meu_gato = Gato("Siamês", "Groot")
print(meu_gato.raca)
print(meu_gato.nome)
meu_gato.falar()

