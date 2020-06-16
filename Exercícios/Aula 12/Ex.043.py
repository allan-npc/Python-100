weight = float(input('Digite seu peso: '))
height = float(input('Digite sua altura: '))
imc = round(weight/(height*2))

if imc <= 18.5:
    print(f'Você está abaixo do peso. IMC = {imc}')
elif imc > 18.5 and imc <= 25:
    print(f'Você está no peso ideal. IMC = {imc}')
elif imc > 25 and imc <= 30:
    print(f'Você está acima do peso gordão. IMC = {imc}')
elif imc > 30 and imc <= 40:
    print(f'Faça seu testamento bola de gordura. IMC = {imc}')
else:
    print(f'Veja o fantasma de uma baleia. IMC = {imc}')