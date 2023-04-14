from tabelas import Dados
from individuo import Individuo
import random

class Populacao:
    def __init__(self, individuo : Individuo, tamanho):
        self.populacao = [Individuo()]*tamanho
        self.fitness = 0

    def fitness_populacao(self, individuo : Individuo):
        return individuo.fitness()
    
    def mutacao(self):
        nova_populacao = []
        for i in self.populacao:
            nova_populacao.append(i.mutacao())

        return nova_populacao
    
    def crossover(self):
        return 0 #implementar
    
    def selecao(self, populacao1, populacao2):
        return 0 #implementar


ind = Individuo(Dados())