from abc import ABC, abstractmethod

class Transacao(ABC):
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

    @abstractmethod
    def registrar(self, conta):
        pass

    def __str__(self):
        return f"{self.tipo}: R$ {self.valor:.2f}"