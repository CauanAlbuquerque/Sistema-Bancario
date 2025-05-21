from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, conta, transacao):
        # registrar vai ser definido na classe abstrata chamada transação
        transacao.registrar(conta) 
        
    def adicionar_conta(self, conta):
        return self.conta.append(conta)
    
    
class Transacao(ABC):
    def registrar(self, conta):
        pass