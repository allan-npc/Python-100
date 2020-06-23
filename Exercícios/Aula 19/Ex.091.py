# importar randint do módulo random
from random import randint
#importar sleep do módulo time
from time import sleep
# Declarar dicionário e váriaveis
jogos = {}
jogadores = 1
# Rolagem de dado dos quatro jogadores
for Jogador in range(0,4):
    jogos[f'Jogador {jogadores}'] = randint(1,6)
    jogadores += 1
    jogos.copy()
# Impressoão das rolagens
for k, v in jogos.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('Ranking dos jogadores')
print('-'*30)
# Impressão do rank
jogadores = 1
for k, v in sorted(jogos.items(), key=lambda x:x[1], reverse=True):
    print(f'{jogadores}° lugar: {k} tirou {v}')
    jogadores += 1
print('-'*30)