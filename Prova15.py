class Veiculo:
    def __init__(self):
        pass
        
    def movimentar(self):
        print('Veículo está em movimento.')

meu_veiculo = Veiculo()
meu_veiculo.movimentar()

class Carro(Veiculo):
    def __init__(self, modelo):
        self.modelo = modelo
        

    def movimentar(self):
        print(f'O carro {self.modelo} está dirigindo!')

meu_carro = Carro("Uno")
meu_carro.movimentar()

class Moto(Veiculo):
    def __init__(self, modelo):
        self.modelo = modelo
    
    def movimentar(self):
        print(f'A moto {self.modelo} está acelerando!')

minha_moto = Moto("Kawasaki")
minha_moto.movimentar()

