from tabelas import Dados
import numpy as np
import random
import copy

class Individuo:
    def __init__(self, dados : Dados, rota = None):
        self.dados = dados
        self.rota = rota
        if rota == None:
            self.rota = self.rand_rota()

        self.peso = self.peso_roubo()
        self.valor = self.valor_roubo()
        self.tempo = self.tempo_roubo()
        self.fit = self.fitness()


    #geramos uma lista de numeros aleatorios de acordo com a qtd de cidades e usamos ela para pegar cidades aleatorias do csv
    def rand_rota(self):
        rota = []
        rota.append('Escondidos')
        cidades = self.dados.cidades
        # randoms = random.sample(range(len(cidades)), len(cidades))
        randoms = np.random.choice(cidades, len(cidades), replace=False)
        while randoms[0] == 'Escondidos' or randoms[1] == 'Escondidos':
            randoms = np.random.choice(cidades, len(cidades), replace=False)
        
        for elemento in randoms:
            rota.append(elemento)
            
        return rota

    #mudar aleatoriamente duas cidades menos a primeira e segunda que é escondidos sempre
    def mutacao(self):
        rota = copy.deepcopy(self.rota)
        qtd_cidades = 2
        randoms = random.sample(range(1, len(rota)), qtd_cidades)
        #trocando de poisçao as cidades que foram aleatoriamente escolhidas
            
        r0 = rota[randoms[0]]
        r1 = rota[randoms[1]]
        
        rota[randoms[0]] = r1
        rota[randoms[1]] = r0
        
        if rota[1] == 'Escondidos':
            return self.mutacao()

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
        

    def rota_de_verdade(self):
        rota= []
        i = 1
        rota.append(self.rota[0])
        while self.rota[i] != 'Escondidos':
            rota.append(self.rota[i])
            i += 1
        rota.append(self.rota[i])
        return rota
    
    def tempo_roubo(self):
        tempo = 0
        rd = self.rota_de_verdade()
        r = self.dados.rotas
        
        for i in range(len(rd) - 1):
            tempo += r[rd[i]][rd[i+1]]['tempo_transporte']

        return tempo
    
    def custo_roubo(self):
        custo = 0
        rd = self.rota_de_verdade()
        r = self.dados.rotas
        
        for i in range(len(rd) - 1):
            custo += r[rd[i]][rd[i+1]]['custo']
        return 0

    #usar para calcular peso e valor ja que escondidos nao tem nada ent precisamos so da rota entre os dois para calculo de valor e peso
    def rota_sem_escondidos(self):
        rota= []
        i = 1
        while self.rota[i] != 'Escondidos':
            rota.append(self.rota[i])
            i += 1
        return rota
    
    def valor_roubo(self):
        roubado = self.dados.itens
        rota = self.rota_sem_escondidos()
        valor_roubado = 0
        
        for cidade in rota:
            valor_roubado += roubado[cidade]['valor']
        
        return valor_roubado
    
    def peso_roubo(self):
        roubado = self.dados.itens
        rota = self.rota_sem_escondidos()
        peso_roubado = 0
        
        for cidade in rota:
            peso_roubado += roubado[cidade]['peso']
        
        return peso_roubado
    
#   def lucro(self):
#       return self.valor_roubo() - self.custo_roubo()
    
    def fitness(self):
        if self.check_rota() == False:
            return float('-inf')
        if self.peso_roubo() > 20:
            return float('-inf')
        if self.tempo_roubo() > 72:
            return float('-inf')
        
        
        return self.valor_roubo() - self.custo_roubo()


# TESTES

""" data = Dados()
ind = Individuo(data)
print(ind.rota)
r2= ind.rota_de_verdade()
r3 = ind.valor_roubo()
r4 = ind.peso_roubo()
r5 = ind.tempo_roubo()
print(r2)
print(r3, r4, r5) """