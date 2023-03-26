from AlunosMatriculados import AlunosMatriculados

alunos = []


while True:
    print("Selecione uma opção:")
    print("[a] Adicionar aluno")
    print("[m] Calcular a média de um aluno")
    print("[f] Descobrir a nota necessária na prova final")
    print("[l] Listar alunos")
    print("[s] Sair")
    opcao = input("Opção: ")

    if opcao == 'a':
        matricula = input("Digite o número da matricula: ")
        nome = input("Digite o nome: ")
        nota1 = input("Digite a nota da primeira prova: ")
        nota2 = input("Digite a nota da segunda prova: ")
        notaTrabalho = input("Digite a nota do trabalho: ")
        alunos.append(AlunosMatriculados(matricula, nome, nota1, nota2, notaTrabalho))
    elif opcao == 'm':
        nome = input("Qual o nome do aluno: ")
        for i in alunos:
            if i.nome == nome:
                i.media()
    elif opcao == 'f':
        nome = input("Qual o nome do aluno: ")
        for i in alunos:
            if i.nome == nome:
                i.final()
    elif opcao == 'l':
        for i, aluno in enumerate(alunos):
                print(f"{i} Matricula = {aluno.matricula}")
                print(f"Nome = {aluno.nome}")
                print(f"Nota da primeira prova = {aluno.nota1}")
                print(f"Nota da segunda prova = {aluno.nota2}")
                print(f"Nota do trabalho = {aluno.notaTrabalho}") 
    elif opcao == 's':
        break
    else:
        print("Por favor, digite uma opção válida.") 

