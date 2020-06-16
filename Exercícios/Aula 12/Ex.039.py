from datetime import date
year = date.today().year
b_year = int(input('Digite ano de nascimento: '))
age = year - b_year

if age <= 45 and age >=18:
    print(f'Parabéns você tem {age} anos e está apto para o alistamento militar.')
# elif age > 45 or age < 18:
#     print('Infelizmente você não está apto para o alistamento militar')
elif age < 18:
    print (f'Você possui {age} anos e ainda faltam mais {abs(age-18)} ano(s) para que você possa se alistar.')
else:
    print(f'Infelizmente você passou em {age-45} anos a data limite de alistamento militar.')