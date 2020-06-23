def ficha(a="Não informado", b = 0):
    if b.isnumeric():
        b = int(b)
    else:
        b = 0
    if a.strip() == '':
        a = 'Não Informado'
    else:
        a = str(a)
    print(f'O jogador {a} fez {b} gol(s) no campeonato.')
    # print('-='*30)
    # print(f'{a:>30}')
    # print(f'{b:>30}')

name = input('Nome do Jogador: ')
age = input('Número de Gols: ')
ficha(name,age)