import os

lista_compras = []
class Compra:

    def __init__(self, produto, preco, quantidade):
        self.produto = produto
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_compra(self, Compra):
            lista_compras.append(Compra)

    def finalizar_compra():
        total = 0
        for compra in lista_compras:
            total += float(compra.preco) * int(compra.quantidade)
        print(f"O valor total da compra foi: {total} Reais")

    def remover_compra(produto_digitado):
        for i, produto in enumerate(lista_compras):
            if produto.produto == produto_digitado:
                print(f"O produto {produto.produto} possui {produto.quantidade} quantidades")
                quantidade_desejada_retirada = input("Digite a quantidade que deseja retirar: ")
            try:
                if int(quantidade_desejada_retirada) == int(produto.quantidade):
                    del lista_compras[i]
                if int(quantidade_desejada_retirada) < int(produto.quantidade):
                    produto.quantidade = produto_digitado
            except ValueError:
                print("Por favor, digite uma quantidade existente")

    def listar_compras():
        print(f"{lista_compras}")
        os.system("cls")
        if len(lista_compras) == 0:
            print("Nenhuma compra registrada. ")
        else:
            for i, compra in enumerate(lista_compras):
                print(f"{i} - Produto: {compra.produto} | Preço: R${compra.preco} | Quantidade: {compra.quantidade}") 