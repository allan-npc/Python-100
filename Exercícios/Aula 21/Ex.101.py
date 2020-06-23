from datetime import date

def voto(ano):
    anovoto = date.today().year - ano
    return(anovoto)

age = int(input('Digite seu ano de nascimento: '))
if voto(age) < 16:
    print(f'Você tem {voto(age)} anos e é menor de idade, direito a voto negado: ')
elif voto(age) >= 18 and voto(age) <= 70:
    print(f'Você tem {voto(age)} anos. Corra para as urnas ou pague multa.')
else:
    print(f'Você tem {voto(age)} anos, seu voto é opcional.')