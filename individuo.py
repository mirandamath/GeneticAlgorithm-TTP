from tabelas import Dados
import random

class Individuo:
    def __init__(self, dados : Dados, rota = None):
        self.dados = dados
        self.rota = rota
        if rota == None:
            self.rota = self.rand_rota()

        self.fit = self.fitness()

    def rand_rota(self):
        rota = []
        cidades = self.dados.cidades
        randon_list = random.sample(range(len(cidades)), len(cidades))
        rota.append('Escondidos')
        for i in range(13):
            rota.append(cidades[randon_list[i]])
        rota[-1] = rota[0]
        return rota

    def fitness(self):
        return 0 #implementar

    def mutacao(self):
        return 0 #implementar
    

# TESTES

data = Dados()
ind = Individuo(data)
r = ind.rand_rota()
print(r)