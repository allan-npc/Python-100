# age = int(input('Digite sua idade: '))
# sex = input('Digite seu sexo [M/F]: ').strip()
age_t = sex_m = sex_f = 0
c = 'S'
while c not in 'Nn':
    age = int(input('Digite sua idade: '))
    sex = input('Digite seu sexo [M/F]: ').strip()
    if age > 18:
        age_t += 1
    if sex in 'Mm':
        sex_m += 1
    if sex in 'Ff' and age > 20:
        sex_f += 1    
    c = input('Deseja continuar? [S/N] \n').strip()
print(f'{age_t} tem mais de 18 anos\n {sex_m} homens foram cadastrados\n {sex_f} mulheres com mais de 20 foram cadastradas')