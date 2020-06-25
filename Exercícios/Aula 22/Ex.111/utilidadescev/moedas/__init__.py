def moeda(preço = 0, moeda = 'R$', format = False):
    return f'{moeda}{preço:>.2f}'. replace('.',',')

def aumentar(a = 0,b = 0, format = False):
    aument = (b/100) * a + b
    if format:
        return moeda(aument)
    else:
        return aument

def diminuir(a = 0,b = 0, format = False):
    dimin = a - (a/100) * b
    if format:
        return moeda(dimin)
    else:
        return dimin

def dobro(a = 0, format = False):
    db = a * 2
    if format:
        return moeda(db)
    else:
        return db

def metade(a = 0, format = False):
    met = a / 2
    if format:
        return moeda(met)
    else:
        return met

def resumo(a = 0, b = 0, c = 0, format = True):    
    print('-'*36)
    print('RESUMO DO VALOR'.center(36))
    print('-'*36)
    print(f'Preço analisado: \t{moeda(a):>}')
    print(f'Dobro do preço: \t{dobro(a,True):>}')
    print(f'Metade do preço: \t{metade(a,True):>}')
    print(f'{b}% do preço: \t\t{aumentar(a,b,True):>}')
    print(f'{c}% do preço: \t\t{diminuir(a,c,True):>}')
    print('-'*36)