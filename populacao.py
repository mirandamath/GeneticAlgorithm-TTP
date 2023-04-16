from tabelas import Dados
from individuo import Individuo
import copy
from tabelas import Dados

class Populacao:
    def __init__(self, tamanho):
        self.n = tamanho
        self.populacao = [Individuo(Dados()) for i in range(tamanho)]

        

    def fitness_populacao(self):
        list = []
        for ind in self.populacao:
            fit = ind.fitness() 
            list.append(fit)
        return list
    
    def mutacao(self):
        mutados = []
        for individuo in copy.deepcopy(self.populacao):
            mutado = individuo.mutacao()
            mutados.append(mutado)
        return mutados

    def crossover(self):
        new_pop = []
        new_ind = []

        mid = len(self.populacao) // 2

        # primeira parte seria index 0 (tem escondidos) até o segundo escondidos
        # e l e    l a e

        pop_direita = self.populacao[:mid]
        pop_esquerda = self.populacao[mid:]

        for i in range(mid):
            rota_esquerda = pop_direita[i].rota_de_verdade()
            rota_direita = pop_esquerda[i].rota_de_verdade()

            rota_direita = rota_direita[len(rota_direita) // 2:]
            rota_esquerda = rota_esquerda[:len(rota_esquerda) // 2]

            for cidade in Dados().get_cidades():
                if rota_direita.count(cidade)  ==  1 and rota_esquerda.count(cidade) == 0:
                    rota_final = (rota_direita + rota_esquerda)
                elif rota_direita.count(cidade)  ==  0 and rota_esquerda.count(cidade) == 1:
                    rota_final = (rota_direita + rota_esquerda)
                    

            new_ind.append(rota_final)

        for individuo in new_ind:
            new_pop.append(Individuo(Dados(), individuo))
        
        return new_pop
    
    def top_individuo(self):
        # nova_lista = sorted(self.populacao, key=self.fitness_pop ,reverse= True) 
        return self.populacao[0]
    
    def top_fitness(self):
        # nova_lista = sorted(self.populacao, key=self.fitness_populacao(), reverse=True)
        return self.top_individuo().fitness()
    
    # populacao mutada e popualcao crossover
    def sort_pop(self):
        # ordenar a população de acordo com o fitness
        sorted_pop = []
        # adicionar o primeiro individuo da população
        sorted_pop.append(self.populacao[0])

        # percorrer sorted_pop e comparar o fitness atual com os outros
        for i in range(1, len(self.populacao)):
            for j in range(len(sorted_pop)):
                if self.populacao[i].fitness() > sorted_pop[j].fitness():
                    # se pop[i] for maior queremos colocar antes de sorted_pop[j], pois o fitness dele eh melhor
                    sorted_pop.insert(j, self.populacao[i])
                    break
                # se o fitness for menor, queremos colocar por ultimo
                elif j == len(sorted_pop) - 1:
                    sorted_pop.append(self.populacao[i])
                    break
        return sorted_pop
        
            

    def selecionar(self, pop_mutada, pop_crossover):
        pop_total = self.populacao + pop_mutada + pop_crossover
        # fazer uma lista ordenada com os fitness de cada individuo
        nova_lista = self.sort_pop()
        # nova_lista = sorted(pop_total, key=self.fitness_populacao(), reverse=True)
        melhores = nova_lista[:self.n]
        self.populacao = melhores
        


# TESTES

def print_populacao(populacao):
    for individuo in populacao:
        print(f'Rota -> {individuo.rota}')
        print(f'\t Peso {individuo.peso}')
        print(f'\t Tempo {individuo.tempo}')
        print(f'\t Valor {individuo.valor}')


""" pop = Populacao(Individuo, 10)
print(pop.crossover())
# m = pop.mutados()
# print_populacao(pop.populacao)
# print("==================================")
# print_populacao(m) """