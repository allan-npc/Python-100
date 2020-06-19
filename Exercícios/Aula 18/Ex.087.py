matriz = []
linha = []
soma = maior = 0

for l in range(0,3):
    for n in range(0,3):
        linha.append(int(input('Digite o valor: ')))        
    matriz.append(linha[:])
    linha.clear()
    print('Próxima linha')
print('Aqui está a matriz: ')
for p in matriz:
    print(f'{p[0]} {p[1]} {p[2]}')
# A soma de todos os valores pares
for l in range(0,3):
    for n in range(0,3):
        if matriz[l][n] % 2 == 0:
            soma += matriz[l][n]
# Maior da Segunda linha
for p in range(0,3):
    if p == 0:
        maior = matriz[1][p]
    elif matriz[1][p] > maior:
        maior = matriz[1][p]

print(f'A soma de todos os valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'{maior} é o maior valor da segunda linha')