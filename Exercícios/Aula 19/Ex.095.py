# Variáveis
jogadores = []
jog_dic = {}
gols_list = []
contador = 1
while True:
    jog_dic['cod'] = len(jogadores)+1
    jog_dic['Nome'] = input('Digite o nome do jogador: ').capitalize()
    jog_dic['Partidas'] = int(input(f'Quantas partidas {jog_dic["Nome"]} jogou? '))
    for gol in range(0, jog_dic['Partidas']):
        gols_list.append(int(input(f'Quantos gols {jog_dic["Nome"]} marcou na partida {contador}? ')))
        contador += 1
    jog_dic['Gols'] = gols_list[:]
    jogadores.append(jog_dic.copy())
    jog_dic.clear()
    gols_list.clear()   
    contador = 1 
    while True:
        cont = input('Deseja continuar [S/N]').capitalize()
        if cont in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if cont == 'N':
        break
print('-='*30)
for k, v in enumerate(jogadores):
    for d in v.keys():
        print(f'{str(d):<15}', end='')
    print()

print('-'*60)
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*60)

while True:
    mais = int(input('Mostrar dados de qual jogador? (999) para parar: '))    
    if mais == 999:
        print('\nFIM')
        break
    if mais >= len(jogadores)+1:
        print(f'Erro! não existe jogador com o código {mais}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[mais-1]["Nome"]}')
        for i, g in enumerate(jogadores[mais-1]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols')