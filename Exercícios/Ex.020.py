import random
# Digita o nome dos alunos
n1 = int(input('Digite a quantidade de candidatos: '))
grupo = []

# Verifica quantos nomes foram digitados e adiciona em uma lista
# Sorteia um dentre a lista
for index in range(n1):
    grupo.append(input('Digite o nome dos alunos a serem sorteados: ').capitalize())

print(f'\n \n A ordem de sorteio foi: {random.choices(grupo,k=n1)}')