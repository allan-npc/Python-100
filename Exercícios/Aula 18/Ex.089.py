alunos = []
dados = []
while True:
    dados.append(input('Digite o nome do aluno: ').capitalize())
    dados.append(int(input('Digite a primeira nota do aluno: ')))
    dados.append(int(input('Digite a segunda nota do aluno: ')))
    alunos.append(dados[:])
    dados.clear()
    r = input('Deseja cadastrar outra pessoa? [S/N] ')
    while r not in 'SsNn':
        r = input('Deseja cadastrar outra pessoa? [S/N] ')
    if r in 'Nn':
        break
# print(alunos)
for alu in alunos:
    print(f'O aluno {alu[0]} teve a média de {(alu[1]+alu[2])/2}\n')

#Escolha aluno e nota
indv = input('Deseja ver as notas individuais de cada aluno? [S/N] ')
# print(indv)
# while indv not in 'SsNn':
#     indv = input('Deseja ver as notas individuais de cada aluno? [S/N] ')
if indv in 'Ss':
    for alu in alunos:
        print(f'O aluno {alu[0]} teve as notas {alu[1]} e {alu[2]}')