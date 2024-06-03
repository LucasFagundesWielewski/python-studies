class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir_no_inicio(self, nome, preco, quantidade):
        novo_produto = Produto(nome, preco, quantidade)
        if not self.cabeca:
            self.cabeca = self.cauda = novo_produto
        else:
            novo_produto.proximo = self.cabeca
            self.cabeca.anterior = novo_produto
            self.cabeca = novo_produto

    def inserir_no_final(self, nome, preco, quantidade):
        novo_produto = Produto(nome, preco, quantidade)
        if not self.cauda:
            self.cabeca = self.cauda = novo_produto
        else:
            novo_produto.anterior = self.cauda
            self.cauda.proximo = novo_produto
            self.cauda = novo_produto

    def remover_produto(self, nome):
        atual = self.cabeca
        while atual:
            if atual.nome == nome:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.cauda = atual.anterior
                return True
            atual = atual.proximo
        return False

    def buscar_produto(self, nome):
        atual = self.cabeca
        while atual:
            if atual.nome == nome:
                return atual
            atual = atual.proximo
        return None

    def imprimir_lista(self):
        atual = self.cabeca
        while atual:
            print(f"Produto: {atual.nome}, Preço: {atual.preco}, Quantidade: {atual.quantidade}")
            atual = atual.proximo

    def imprimir_lista_reversa(self):
        atual = self.cauda
        while atual:
            print(f"Produto: {atual.nome}, Preço: {atual.preco}, Quantidade: {atual.quantidade}")
            atual = atual.anterior

# Exemplo de uso
lista = ListaDuplamenteEncadeada()
lista.inserir_no_inicio("Maçã", 2.50, 100)
lista.inserir_no_final("Banana", 1.20, 150)
lista.inserir_no_inicio("Laranja", 3.00, 80)

print("Lista de Produtos:")
lista.imprimir_lista()

print("\nLista de Produtos (Reversa):")
lista.imprimir_lista_reversa()

produto = lista.buscar_produto("Banana")
if produto:
    print(f"\nProduto encontrado: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}")
else:
    print("\nProduto não encontrado.")

if lista.remover_produto("Laranja"):
    print("\nProduto Laranja removido com sucesso.")
else:
    print("\nProduto Laranja não encontrado.")

print("\nLista de Produtos após remoção:")
lista.imprimir_lista()
