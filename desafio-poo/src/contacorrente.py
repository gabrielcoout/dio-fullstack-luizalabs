from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, cliente, limite=500, limite_saques=3):
        super().__init__(agencia, numero_conta, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo and self.numero_saques < self.limite_saques:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            return True
        else:
            print("Operação falhou! O valor informado é inválido ou limite de saques atingido.")
            return False