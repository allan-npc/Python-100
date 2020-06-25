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
        return(dimin)
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
        return(met)
    else:
        return met