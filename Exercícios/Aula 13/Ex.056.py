age_all = []
name_old = '' 
maioridade = 0
age_w = 0
for data in range(1,5):
    name = str(input('Digite o seu nome: ')).capitalize()
    age = int(input('Digite sua idade: '))
    age_all.append(age)
    sex = str(input('Digite seu sexo: ')).upper()
    if sex == 'M' and data == 1:
        maioridade = age
        name_old = name
    if sex == 'M' and age > maioridade:
        maioridade = age
        name_old = name
    if sex == 'F' and age < 20:
        age_w =+ 1

print(f'A média das idades é: {sum(age_all)/len(age_all)}')
print(f'{name_old} é o homem mais velho')
print(f'{age_w} mulheres tem menos de 20 anos de idade')