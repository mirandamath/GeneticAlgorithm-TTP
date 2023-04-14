from tabelas import Dados

class Individuo:
    def __init__(self, dados : Dados, rota = None):
        self.dados = dados
        self.rota = rota
        if rota == None:
            self.rota = self.rand_rota()

        self.fit = self.fitness()

    def rand_rota(self):
        return 0 #implementar rota aleatoria

    def fitness(self):
        return 0 #implementar

    def mutacao(self):
        return 0 #implementar
    