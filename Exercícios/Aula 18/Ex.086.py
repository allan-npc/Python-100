matriz = []
linha = []
for l in range(0,3):
    for n in range(0,3):
        linha.append(int(input('Digite o valor: ')))
    matriz.append(linha[:])
    linha.clear()
    print('Próxima linha')
print('Aqui está a matriz: ')
for p in matriz:
    print(f'{p[0]} {p[1]} {p[2]}')