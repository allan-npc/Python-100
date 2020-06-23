#Váriaveis, dicionários e listas
dados = {}
compilado = []
cadn = midade = 0
while True:
    dados['nome'] = input('Nome: ').capitalize()
    dados['sexo'] = input('Sexo [M/F]: ').capitalize()     
    dados['idade'] = int(input('Idade: '))
    midade += dados['idade']
    cont = input('Deseja continuar? [S/N] ')
    compilado.append(dados.copy())
    cadn +=1
    if cont in 'Nn':
        break
    dados.clear()
print(f'a) Foram cadastradas {cadn} pessoas')
print(f'b) A média de idade é de {midade/cadn}')
for m in compilado:
    if m['sexo'] in 'Ff':
        print(f'c) Essas são as mulheres cadastradas: {m}')
for age in compilado:
    if age['idade'] >= midade/cadn:
        print(f'd) Essas são as pessoas com idade acima da média: {age}')
# print(dados)
# print(compilado)    