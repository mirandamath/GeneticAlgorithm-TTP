from tabelas import Dados
import random

class Individuo:
    def __init__(self, dados : Dados, rota = None):
        self.dados = dados
        self.rota = rota
        if rota == None:
            self.rota = self.rand_rota()

        self.fit = self.fitness()


    #geramos uma lista de numeros aleatorios de acordo com a qtd de cidades e usamos ela para pegar cidades aleatorias do csv
    def rand_rota(self):
        rota = []
        cidades = self.dados.cidades
        randoms = random.sample(range(len(cidades)), len(cidades))
        rota.append('Escondidos')
        for i in range(13):
            rota.append(cidades[randoms[i]])
        #forçar escondidos a ser a ultima posição é opcional 
        # caso nao seja considera-se como rota ate a posiçao que escondidos se encontra  caso seja considera-se rota ate a ultima posiçao
        #rota[-1] = rota[0]
        return rota

    #mudar aleatoriamente duas cidades menos a primeira e segunda que é escondidos sempre
    def mutacao(self):
        rota = self.rota
        qtd_cidades = 2
        randoms = random.sample(range(1, len(rota)), qtd_cidades)
        #trocando de poisçao as cidades que foram aleatoriamente escolhidas
        rota[randoms[0]] = rota[randoms[1]]
        rota[randoms[1]] = rota[randoms[0]]
        
        return Individuo(self.dados, rota)
    
    
    def check_rota(self):
        #verififcar se escondidos é a primeira
        if self.rota[0] != "Escondidos":
            return False
        #se escondidos é a ultima cidade
        #if self.rota[-1] != "Escondidos":
            #return False
        
        #escondidos tem que aparecer 2 vezes
        if self.rota.count('Escondidos') < 2:
            return False

        # escondidos nao pode ser a segunda cidade pois tem que ter pelo menos uma cidade entre o primeiro e segundo escondidos
        if self.rota[1] == 'Escondidos':
            return False
        

    
    def fitness(self):
        return 0 #implementar
    

# TESTES

data = Dados()
ind = Individuo(data)
r = ind.rand_rota()
print(r)