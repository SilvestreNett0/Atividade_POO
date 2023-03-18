from Funcoes import adicionar_compra, finalizar_compra, remover_compra, listar_compras

while True:
    print("Selecione uma opção:")
    print("[a] Adicionar compra")
    print("[f] Finalizar compra")
    print("[r] Remover compra")
    print("[l] Listar compras")
    print("[s] Sair")
    opcao = input("Opção: ")

    if opcao == 'a':
        adicionar_compra()
    elif opcao == 'f':
        finalizar_compra()
    elif opcao == 'r':
        remover_compra()
    elif opcao == 'l':
        listar_compras()
    elif opcao == 's':
        break
    else:
        print("Por favor, digite uma opção válida.") 
