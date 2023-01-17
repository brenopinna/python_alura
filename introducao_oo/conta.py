
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = float(saldo)
        self.__limite = float(limite)

    def extrato(self):
        print(f'O saldo do titular {self.__titular} é de R${self.__saldo}')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar


    def saca(self,valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod #metodo da classe (Conta), nao precisa de objeto
    def codigo_banco():
        return '001'

    @staticmethod #metodo da classe (Conta), nao precisa de objeto
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}#dicionario
