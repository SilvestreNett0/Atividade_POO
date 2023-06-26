menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":

        valor = float(input("Informe o valor desejado para o saque: "))

        if(valor > saldo):
            print("Não há saldo suficiente")
        
        elif(valor > limite):
            print("O valor do saque é maior que o limite")
        
        elif(numero_saques >= LIMITE_SAQUES):
            print(f"Número de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    
        else:
            print("Valor informado é invalido")

    elif opcao == "3":
        print("\n===========EXTRATO===========")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================")
    
    elif opcao == "0":
        break

    else:
        print("Operacação invalida")