palavras = ('carro', 'programacao', 'curso', 'sagaz', 'teste', 'exercicio')

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for v in p:
        if v in 'aeiou':
            print(v, end=' ')