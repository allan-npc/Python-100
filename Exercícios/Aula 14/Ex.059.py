n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = int(input('Escolha a operação a ser efetuada\n [1] Soma\n [2] Multiplicação\n [3] Maior número\n [4] Novos números\n [5] Sair do programa\n'))
while op != 5:
    if op == 1:
        print(f'O resultado de {n1} + {n2} = {n1 + n2}')
    if op == 2:
        print(f'O resultado de {n1} * {n2} = {n1 * n2}')
    if op == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    if op == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    op = int(input('Escolha a operação a ser efetuada\n [1] Soma\n [2] Multiplicação\n [3] Maior número\n [4] Novos números\n [5] Sair do programa\n'))
print('Fim')