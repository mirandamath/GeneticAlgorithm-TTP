from populacao import Populacao
from tabelas import Dados
import algGenetico


alg = algGenetico.AlgoritmoGeneticoPopulacao(Populacao(100))


melhor_individuo = alg.rodar()

print(f'Rota -> {melhor_individuo.rota_de_verdade()}')
print(f'\t Peso {melhor_individuo.peso}')
print(f'\t Tempo {melhor_individuo.tempo}')
print(f'\t Valor {melhor_individuo.valor}')