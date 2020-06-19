lista = []
lpar = []
limpar = []
while True:
    lista.append(int(input('Digite o número: ')))
    r = input('Deseja continuar? [S/N]: ')
    if r in 'Nn':
        break
for i, v in enumerate(lista):
        if v % 2 == 0:
            lpar.append(v)            
        elif v % 2 == 1:
            limpar.append(v)
print(f'Essa é a lista completa: {lista}')
print(f'Essa é a lista par: {lpar}')
print(f'Essa é a lista ímpar: {limpar}')