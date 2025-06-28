class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque} unidades")

    def preco_final(self):
        return self.preco

    def emitir_nota(self):
        print(f"Nota gerada para {self.nome}.")

    def repor(self, quantidade):
        self.estoque += quantidade
        print(f"{quantidade} unidades adicionadas. Estoque atual: {self.estoque}.")

    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f"{quantidade} unidades vendidas. Estoque restante: {self.estoque}.")
        else:
            print(f"Não há estoque suficiente para vender {quantidade} unidades.")

class ProdutoNacional(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)

    def emitir_nota(self):
        print(f"Nota fiscal nacional para {self.nome}.")

class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)
        self.taxa_importacao = taxa_importacao

    def preco_final(self):
        return self.preco + (self.preco * self.taxa_importacao)

    def emitir_nota(self):
        print(f"Nota de importação para {self.nome} com taxa aplicada.")
