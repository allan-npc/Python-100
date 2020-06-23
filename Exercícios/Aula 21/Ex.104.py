def leiaInt(msg):        
    valor = 0
    while True:
        num = input(msg)
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('\033[0;31mERRO! Digite o número inteiro válido\033[m')        
    return valor


num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')