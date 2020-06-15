s = input('Digite seu nome completo: ')
sp = s.split()
# Nome com todas as letras maiusculas
print(f'Seu nome com todas as letras maiusculas: {s.upper()}')
# Nome com todas as letras minusculas
print(f'Seu nome com todas as letras minusculas: {s.lower()}')
# Quantidade de letras no nome
print(f'Quantidade de letras em seu nome: {len(s)}')
# Quantidade de letras no primeiro nome
print(f'Quantidade de letras em seu primeiro nome: {len(sp[0])}')