def lis():
    print('-'*60)
    print('PESSOAS CADASTRADAS'.center(60))
    print('-'*60)

    with open('cadastrodb.txt') as cad:
        data = cad.read()
    print(data)