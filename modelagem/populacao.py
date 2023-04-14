from tabelas import Dados
from individuo import Individuo

class Populacao:
    def __init__(self, individuo : Individuo, tamanho):
        self.populacao = [Individuo()]*tamanho
        self.fitness = 0

    def fitness_populacao(self, individuo : Individuo):
        return 0 #implementar
    
    def mutacao(self):
        return 0 #implementar
    
    def crossover(self):
        return 0 #implementar
    
    def selecao(self, populacao1, populacao2):
        return 0 #implementar


# TESTES
ind = Individuo(Dados())