def area(a,b):
    ter = a * b
    print(f'A Área de um terreno de {larg} x {prof} é de {ter}')

print('CONTROLE DE TERRENOS')
print('-'*30)

larg = float(input('Largura (m): '))
prof = float(input('Profundidade (m): '))

area(larg,prof)