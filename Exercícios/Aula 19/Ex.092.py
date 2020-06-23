# Importar datetime
from datetime import datetime
# Dicionário e variáveis
dados = {}
dados['nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
# print(dados)
if dados['ctps'] == 0:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    dados['anoc'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = (35 + dados['anoc']) - nasc
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
print(dados)