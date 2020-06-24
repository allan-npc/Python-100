def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (separado por ,)
    :param sit: opcional indicando aprovação ou reprovação do aluno (True)
    :return: Dicionário criado
    """
    for n in notas_list:
        if n > MAIOR_NOTA:
            MAIOR_NOTA = n
        if n < MENOR_NOTA:
            MENOR_NOTA = n
    notas_dic['Total'] = len(notas)
    notas_dic['Maior'] = max(notas)
    notas_dic['Menor'] = min(notas)
    notas_dic['Media'] = sum(notas)/len(notas)
    if sit:
        if notas_dic['Media'] >= 6:
            notas_dic['Situação'] = 'Aprovado'
        else:
            notas_dic['Situação'] = 'Reprovado'
    return notas_dic


notas_dic = {}
notas_list = []
notas(5.5, 6, 8, sit=True)
print(notas_dic)


### Allan ##$
# def notas():
#     MAIOR_NOTA = MENOR_NOTA = NOTA = 0
#     QTN = int(input('Quantas notas seram inseridas no sistema? '))
#     for NOTAS in range(0,QTN):
#         NOTA = float(input(f'Digite a {NOTAS+1}ª nota: '))
#         notas_list.append(NOTA)
#         MENOR_NOTA = NOTA
#         if NOTA > MAIOR_NOTA:
#             MAIOR_NOTA = NOTA
#         if NOTA < MENOR_NOTA:
#             MENOR_NOTA = NOTA
#     # while True:
    
#     notas_dic['Maior'] = MAIOR_NOTA
#     notas_dic['Menor'] = MENOR_NOTA
#     notas_dic['Media'] = sum(notas_list)/len(notas_list)    
#     if notas_dic['Media'] >= 6:
#         notas_dic['Situacao'] = 'Aprovado'
#     else:
#         notas_dic['Situacao'] = 'Reprovado'

# notas_dic = {}
# notas_list = []

# notas()
# print(f'Dicionário {notas_dic}\n')
# print(f'\n Lista pós sorted {notas_list}')
