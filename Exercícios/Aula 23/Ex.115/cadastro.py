pessoas = {}
def cadastrop(nome, idade):    
    okn = oki = False
    while not okn:
        nome = input('Digite o nome: ').strip().title()                
        if nome.strip() == '':
            print('Nome não informado')            
        else:
            break
    while not oki:
        idade = input('Digite a idade: ')
        if idade.isnumeric():
            idade = int(idade)
            break
        else:
            print('\033[33mErro! idade deve ser cadastrada corretamente\33[m')
    pessoas['Nome'] = nome
    pessoas['Idade'] = idade
    print('Dados cadastrados com sucesso')
    with open('cadastrodb.txt', 'a') as cad:
        # cad.write(f'\'{nome}\' \'{idade}\'\n')
        cad.write(f'{nome};{idade}\n')


# cadastro('allan',37)
# print(pessoas)

# Escrever no arquivo
    # fh = open('Exercícios\Aula 23\Ex.115\cadastrodb.txt', w)
    # fh.write(f'{nome} {idade}')
    # fh.close()