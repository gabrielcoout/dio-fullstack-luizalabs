from transacao import Transacao

class Historico:
    def __init__(self):
        self.historicos = []

    def adicionar_transacao(self, transacao: Transacao):
        self.historicos.append(transacao)