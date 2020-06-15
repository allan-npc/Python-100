km = int(input('Digite a velocidade do carro: '))
lim = int(input('Digite o limite da via: '))
if km <= lim:
    print(f'Parabéns, você estava abaixo de {lim}km/h continue seguindo as leis de trânsito')
else:
    print(f'Você estava {km - lim}km/h acima do limite da via, sua multa será de R${(km - lim)*7:.2f}')