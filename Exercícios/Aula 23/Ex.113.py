def leiaInt(nint):
    while True:
        try:
            numint = int(input(nint))
        except(KeyboardInterrupt):
            print('\033m[0;31 ERRO! Nada foi digitado\033')
        except(ValueError, TypeError):
            print('\033m[0;31 ERRO! Digite um valor inteiro\033')
        else:
            print(f'Você acabou de digitar o número inteiro {numint}')            
            break
    return numint
        

def leiaFloat(nfloat):    
    while True:
        try:
            numfloat = float(input(nfloat).replace(",","."))
        except(KeyboardInterrupt):
            print('\033[31mERRO! Nada foi digitado\033[m')
        except(ValueError, TypeError):
            print('\033[31mERRO! Digite um valor inteiro\033[m')
        else:
            print(f'Você acabou de digitar o número real {numfloat}')            
            break
    return numfloat

numint = leiaInt('Digite um número inteiro: ')
numfloat = leiaFloat('Digita um número real: ')