from random import randint

jogos = []
jogo = []
jdor = int(input('Quantos jogos devem ser gerados? '))

for j in range(0,jdor):
    for n in range(0,6):
        jogo.append(randint(1,25))
    jogos.append(jogo[:])
    jogo.clear()
for ji in jogos:
    print(f'Os jogos gerados são {ji}')