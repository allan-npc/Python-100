def lis():
    print('-'*60)
    print('PESSOAS CADASTRADAS'.center(60))
    print('-'*60)

    with open('cadastrodb.txt') as cad:
        for linha in cad:
            data = linha.split(';')
            print(f'{data[0].center(30)} \t\t\t{data[1]}')
        # data = cad.read()