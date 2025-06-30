class ContaBancaria:
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.__titular = titular
    
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular

    
    def depositar(self, valor):
        
        if valor > 0:
            self.__saldo += valor
            print(f'Deposito de R${valor:.2f} realizado com sucesso!')
        else:
            print('Valor insuficiente para depósito!')

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso!')
        else:
            print('Saldo insuficiente!')

    def exibir_saldo(self):
        print(f'Saldo atual: {self.__saldo:.2f}')
        
minha_conta = ContaBancaria(1000, 'Thais M Silva')
print(minha_conta.get_titular())
minha_conta.depositar(400)
minha_conta.sacar(150)
minha_conta.exibir_saldo()

    
    

