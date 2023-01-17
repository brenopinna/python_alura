from abc import ABCMeta, abstractmethod
from operator import attrgetter
from functools import total_ordering

class Conta(metaclass=ABCMeta): #esse ABC e o absmethod são pra forçar a implementacao
    def __init__(self, codigo):  # de uma funcao nas classes filhas
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f'[>>>Código: {self._codigo} ||| Saldo : {self._saldo}]'

class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass#essa foi só p mostrar o abs method

@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        else:
            return self._codigo < other._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[>>>Código: {self._codigo} ||| Saldo : {self._saldo}]'

contagui = ContaSalario(133)
contagui.deposita(500)

contabrenin = ContaSalario(1700)
contabrenin.deposita(500)

contazeca = ContaSalario(3)
contazeca.deposita(1000)

contas = [contabrenin, contazeca, contagui]
for conta in sorted(contas):
    print(conta)

print(contabrenin <= contabrenin)
