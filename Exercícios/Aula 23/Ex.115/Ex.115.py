import cadastro
import listar

op = (1,2,3)
def menu():
    print('-'*60)
    print('MENU PRINCIPAL'.center(60))
    print('-'*60)
    print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[34mCadastrar nova pessoa\033[m')
    print('\033[33m3\033[m - \033[34mSair do Sistema\033[m')
    print('-'*60)

while True:
    menu()
    opcao = int(input('\033[32mSua Opção:\033\n'))
    if opcao not in op:
        print('Por favor digite uma das opções acima')
    if opcao == 1:
        listar.lis()
    if opcao == 2:
        cadastro.cadastrop('Nome','Idade')
    if opcao == 3:
        print('Obrigado')
        break