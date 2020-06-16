from datetime import date
year = date.today().year
b_year = int(input('Digite seu ano de nascimento: '))
age = year - b_year
if age <= 9:
    print(f'Você está classificada para a categoria mirim até 9 anos')
elif age > 9 and age <= 14:
    print(f'Você está classificada para a categoria infantil até 14 anos')
elif age > 14 and age <= 19:
    print(f'Você está classificada para a categoria junior até 19 anos')
elif age > 19 and age <= 20:
    print(f'Você está classificada para a categoria sênior até 20 anos')
else:
    print(f'Você está classificada para a categoria master')