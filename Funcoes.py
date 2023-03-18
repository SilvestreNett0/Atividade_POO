from Compras import Compra
import os

lista_compras = []

def adicionar_compra():
    produto = input("Digite o produto: ")
    preco = input("Digite o preco: ")
    quantidade = input("Digite a quantidade: ")
    compra = Compra(produto, int(preco), int(quantidade))
    lista_compras.append(compra)
    print("Compra adicionada com sucesso.")

def finalizar_compra():
    total = 0
    for compra in lista_compras:
        total += compra.preco * compra.quantidade
    print(f"O valor total da compra foi: {total}")

def remover_compra():
    produto_digitado = input("Qual produto deseja retirar: ")
    for i, produto in enumerate(lista_compras):
        if produto.produto == produto_digitado:
            print(f"O produto {produto.produto} possui {produto.quantidade} quantidades")
            quantidade_desejada_retirada = input("Digite a quantidade que deseja retirar: ")
            try:
                if int(quantidade_desejada_retirada) == produto.quantidade:
                    del lista_compras[i]
                if int(quantidade_desejada_retirada) < produto.quantidade:
                    produto.quantidade = produto_digitado
            except ValueError:
                print("Por favor, digite uma quantidade existente")  

def listar_compras():
    os.system("cls")
    if len(lista_compras) == 0:
        print("Nenhuma compra registrada. ")
    else:
        for i, compra in enumerate(lista_compras):
            print(f"{i} - Produto: {compra.produto} | Preço: R${compra.preco:.2f} | Quantidade: {compra.quantidade}") 