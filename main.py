from Compras import Compra

while True:
    print("Selecione uma opção:")
    print("[a] Adicionar compra")
    print("[f] Finalizar compra")
    print("[r] Remover compra")
    print("[l] Listar compras")
    print("[s] Sair")
    opcao = input("Opção: ")

    if opcao == 'a':
        produto = input("Por favor, digite o produto: ")
        preco = input("Por favor, digite o valor do preco: ")
        quantidade = input("Por favor, digite a quantidade: ")
        compra = Compra(produto, preco, quantidade)
        compra.adicionar_compra(compra)
    elif opcao == 'f':
        Compra.finalizar_compra()
    elif opcao == 'r':
        produto_digitado_a_ser_retirado = input("Digite o produto que deseja retirar: ")
        Compra.remover_compra(produto_digitado_a_ser_retirado)
    elif opcao == 'l':
        Compra.listar_compras()
    elif opcao == 's':
        break
    else:
        print("Por favor, digite uma opção válida.") 
