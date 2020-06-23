media = {}
media['nome'] = input('Nome do jogador: ')
part = int(input(f'Quantas partidas {media["nome"]} jogou? '))
tot = []
partn = 1
for jogos in range(0,part):
    tot.append(int(input(f'Quantos gols na partida {partn}: ')))
    media['Gols'] = tot[:]
    partn += 1
    media.copy()
media['Total'] = sum(tot)
print(media)
partn = 1
for k, v in media.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {media["nome"]} jogou {part} partidas.')
for k in tot:
    print(f'=> Na partida {partn}, fez {k} gols.')
print(f'Foi um total de {media["Total"]} gols.')