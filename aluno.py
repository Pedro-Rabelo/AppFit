from usuario import Usuario

class Aluno():

    def __init__(self, peso, altura, horario, nascimento, sexo, info, treino, status=True):
        self.peso = peso
        self.altura = altura
        self.horario = horario
        self.nascimento = nascimento
        self.sexo = sexo
        self.info = info
        self.treino = treino
        self.status = status

    def match(self):
        pass

    def batepapo(self):
        pass
