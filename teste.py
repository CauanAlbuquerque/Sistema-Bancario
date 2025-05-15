class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco
        
    @property 
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self._preco = valor
            
        else:
            print("Preço inválido!")
            
produto = Produto("Mousse", 150)
print(produto.preco)

produto.preco = -50
print(produto.preco)