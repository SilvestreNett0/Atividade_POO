from voo import Voo


voos = []

while True:
    print("Selecione uma opção:")
    print("[a] Adicionar voo")
    print("[v] Verificar disponibilidade de cadeiras")
    print("[l] Listar voos")
    print("[s] Sair")
    opcao = input("Opção: ")

    if opcao == 'a':
        numero = input("Digite o número do voo: ")
        data = input("Digite a data do voo (formato dd/mm/aaaa): ")
        horario = input("Digite o horário do voo (formato hh:mm): ")
        voos.append(Voo(numero, data, horario))
        print("Voo adicionado com sucesso!")
    elif opcao == 'v':
        numero = input("Digite o número do voo: ")
        voo = None
        for v in voos:
            if v.retorna_voo() == numero:
                voo = v
                break
        if voo is None:
            print("Voo não encontrado.")
        else:
            cadeira = input("Digite o número da cadeira: ")
            if voo.verifica(cadeira):
                print("Cadeira disponível.")
            else:
                print("Cadeira ocupada.")
    elif opcao == 'l':
        for v in voos:
            print(f"Voo {v.retorna_voo()} - Data: {v.retorna_data()}, Horário: {v.retorna_horario()}. {v.vagas()} vagas disponíveis.")
    elif opcao == 's':
        break
    else:
        print("Por favor, digite uma opção válida.")
