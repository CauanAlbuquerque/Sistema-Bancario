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
    
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = self.saldo < valor
        
        if excedeu_saldo:
            print("Você não tem dinheiro suficiente na conta! ")
        
        elif valor<0:
            saldo -= valor
            print("\nSaque efetuado com sucesso!")
            return True
                
        else:
            print("Operação falhou! O valor informado é inválido")
        
        return False
    
    def depositar(self, valor):
        saldo = self.saldo
        
        if valor > saldo:
            saldo += valor
            print("\nDepósito efetuado com sucesso!")
            return True
        
        return False
        
        
class Conta_corrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    
    
    
    
    
    
    
    
    
    
    
    
class Historico(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self.transacao = []
        
    def registrar(self):
        
    def adicionar_transacao(self, transacao):
        

    
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass
    