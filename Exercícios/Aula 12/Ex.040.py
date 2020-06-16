n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
nf = (n1+n2)/2
if nf < 5:
    print(f'Parabéns por decepcionar sua família, você foi reprovado. Nota final {nf}.')
elif nf >= 5 and nf <6.9:
    print(f'Parabéns por decepcionar sua família, você foi está em recuperação. Nota final {nf}.')
else:
    print(f'Parabéns você foi aprovado. Nota final {nf}.')