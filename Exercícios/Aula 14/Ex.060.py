n1 = int(input('Digite o número a ser fatorado: '))
nf = n1
f = 1

while nf > 0:
    print(f'{nf}', end='')
    print(' x ' if nf > 1 else ' = ', end='')
    f *= nf
    nf -= 1
print(f'{f}', end='')
print(f'\n{n1}! é igual a {f}')