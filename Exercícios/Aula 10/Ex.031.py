dist = int(input('Qual a distância até o destino: '))
if dist <= 200:
    print(f"O valor da sua passagem é de {round(dist*.5)}")
else:
    print(f"O valor da sua passagem é de {round(dist*.45)}")