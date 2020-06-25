def aumentar(a = 0,b = 0):
    aument = (b/100) * a + b
    return aument

def diminuir(a = 0,b = 0):
    dimin = a - (a/100) * b
    return dimin

def dobro(a = 0):
    db = a * 2
    return db

def metade(a = 0):
    met = a / 2
    return met

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'. replace('.',',')