import csv

class Dados:
    def __init__(self):
        self.cidades = self.get_cidades()
        self.itens = self.get_itens()
        self.rotas = self.get_rotas()

    def get_cidades(self):
        cidades = []
        with open('dados/cidades.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                origem, destino, tempo_transporte, custo = row
                if origem not in cidades:
                    cidades.append(origem)
                if destino not in cidades:
                    cidades.append(destino)

        return cidades
    
    def get_itens(self):
        itens = {}
        with open('dados/itens.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # separando cada coluna do arquivo
                item, peso, tempo_roubo, valor, cidade = row
                peso = int(peso)
                tempo_roubo = int(tempo_roubo)
                valor = int(valor)
                # adicionando o item ao dicionário
                itens[cidade] = {'item': item, 'peso': peso, 'tempo_roubo': tempo_roubo, 'valor': valor}

        return itens
    

    def get_rotas(self):
        rotas = {}
        with open('dados/cidades.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                origem, destino, tempo_transporte, custo_transporte = row
                tempo_transporte = int(tempo_transporte)
                custo_transporte = int(custo_transporte)
                
                # Adicionando rotas, tanto origem -> destino, quanto destino -> origem
                if origem not in rotas:
                    rotas[origem] = {}
                rotas[origem][destino] = {'tempo_transporte': tempo_transporte, 'custo': custo_transporte}

                if destino not in rotas:
                    rotas[destino] = {}
                rotas[destino][origem] = {'tempo_transporte': tempo_transporte, 'custo': custo_transporte}

        return rotas

def print_cidades(cidades):
    count = 0
    for cidade in cidades:
        print(cidade)
        count += 1
    print(f'Número de cidades: {count}')

def print_itens(itens):
    count = 0
    for cidade in itens:
        print(f'{cidade}: {itens[cidade]}')
        count += 1
    print(f'Número de itens: {count}')

def print_rotas(rotas):
    count = 0
    for origem in rotas:
        for destino in rotas[origem]:
            print(f'{origem} -> {destino}: {rotas[origem][destino]}')
        count += 1
    print(f'Número de rotas: {count}')
dados = Dados()

# print_cidades(dados.cidades)
# print_itens(dados.itens)
# print_rotas(dados.rotas)