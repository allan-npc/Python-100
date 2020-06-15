name = input('Digite seu nome completo: ').title().strip()
namesplit = name.split()
print(f'Seu primeiro nome é: {namesplit[0]}')
print(f'Seu ultimo nome é: {namesplit[len(namesplit)-1]}')