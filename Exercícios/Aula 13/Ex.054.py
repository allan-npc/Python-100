from datetime import date
year = date.today().year
t = 0
for a in range(1,8):
    b_year = int(input(f'{a}) Digite o seu ano de nascimento: '))
    if year - b_year < 18:
        t += 1
print(f'{t} ainda não atingiram a maioridade.')