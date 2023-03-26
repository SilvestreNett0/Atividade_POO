class Voo:
    def __init__(self, numero, data, horario):
        self.numero = numero
        self.data = data
        self.horario = horario
        self.ocupacao = [False] * 100

    def proximo_livre(self):
        for i, ocupado in enumerate(self.ocupacao):
            if not ocupado:
                return i + 1
        return None

    def verifica(self, cadeira):
        if int(cadeira) < 1 or int(cadeira) > 100:
            return False
        return not self.ocupacao[int(cadeira) - 1]

    def ocupa(self, cadeira):
        if cadeira < 1 or cadeira > 100:
            return False
        if not self.ocupacao[cadeira - 1]:
            self.ocupacao[cadeira - 1] = True
            return True
        return False

    def vagas(self):
        return self.ocupacao.count(False)

    def retorna_voo(self):
        return self.numero

    def retorna_data(self):
        return self.data
    
    def retorna_horario(self):
        return self.horario
