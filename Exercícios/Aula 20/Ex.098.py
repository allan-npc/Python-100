from time import sleep


def contador(ini, fim, pas):
    print(f'Contando de {ini} até {fim} com passo de {pas}')
    if ini <= fim:
        cont = ini
        while cont <= fim:
            print(f'{cont} ', end='')            
            cont += pas
            sleep(.5)
        print('FIM')
        print('-='*30)
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont} ', end='')            
            cont -= pas
            sleep(.5)
        print('FIM')
        print('-='*30)

contador(1,10,1)
contador(10,0,2)
print(f'Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim2 = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim2,passo)