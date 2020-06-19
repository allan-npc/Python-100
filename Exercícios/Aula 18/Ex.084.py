dados = []
pessoa = []
maior = menor = 0
while True:
    dados.append(input('Digite o nome: '))
    dados.append(float(input('Digite o peso: ')))
    pessoa.append(dados[:])
    dados.clear()
    r = input('Deseja cadastrar outra pessoa? [S/N] ')
    while r not in 'SsNn':
        r = input('Deseja cadastrar outra pessoa? [S/N] ')
    if r in 'Nn':
        break
print(f'Foram cadastradas {len(pessoa)} pessoas.')
for p in pessoa:
    if p[1] >= 100:
        print(f'O maior peso foi de {p[1]}. Peso de {p[0]}')
    elif p[1] <= 70:
        print(f'O menor peso foi de {p[1]}. Peso de {p[0]}')