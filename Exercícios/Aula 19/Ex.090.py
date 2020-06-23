alunos = {}
alunos['Nome'] = input('Digite o nome do aluno: ').capitalize()
alunos['Média'] = float(input('Digite a média do aluno: '))
if alunos['Média'] < 7:
    alunos['Situação'] = 'Reprovado'
else:
    alunos['Situação'] = 'Aprovado'
for k, v in alunos.items():
    print(f'{k} é igual a {v}')