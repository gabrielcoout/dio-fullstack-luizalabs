from transacao import Transacao
from historico import Historico
from cliente import Cliente

class Conta:
    def __init__(self, numero_conta, cliente):
        self.saldo = 0.0
        self.agencia = "0001"
        self.numero = numero_conta
        self.historico = Historico()
        self.cliente = Cliente()

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo and self.numero_saques < self.limite_saques:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            return True
        else:
            print("Operação falhou! O valor informado é inválido ou limite de saques atingido.")
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

    def mostrar_extrato(self):
        print("\n=== Extrato ===")
        print(self.extrato if self.extrato else "Nenhuma movimentação.")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("===============\n")