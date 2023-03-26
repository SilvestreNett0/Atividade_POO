class AlunosMatriculados:

    def __init__(self, matricula, nome, nota1, nota2, notaTrabalho):

        self.matricula = int(matricula)
        self.nome = nome
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.notaTrabalho = float(notaTrabalho)

    def media(self):

        media = (self.nota1 * 2.5 + self.nota2 * 2.5 + self.notaTrabalho * (2/3)) / 3
        print(f"O aluno {self.nome}, matricula {self.matricula} obteve a média {media:.2f}")

    def final(self):
        media = (self.nota1 * 2.5 + self.nota2 * 2.5 + self.notaTrabalho * (2/3)) / 3
        if(media >= 6):
            print("Aluno aprovado direto")
            return 0 
        elif (media >= 3):
            print(f"Aluno precisa de {6 - media} para a prova final")
        else:  
            print(f"Aluno reprovado")

