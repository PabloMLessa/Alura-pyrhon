
class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_desejado):
        valor_disponivel = self.__saldo + self.__limite
        return valor_desejado <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transferir(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)
