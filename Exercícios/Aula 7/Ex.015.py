d = int(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos km foram rodados? '))
pd = d * 60
pkm = km *0.15
print(f'O total a ser pago é de {pd + pkm} reais')