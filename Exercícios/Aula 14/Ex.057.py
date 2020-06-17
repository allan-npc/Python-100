# sex = input('Digite seu sexo [M/F]: ').capitalize()
# while sex not in 'MF':
#     sex = input('Você digitou um sexo inexistente, faça novamente. [M/F]: ').capitalize()


sex = input('Digite seu sexo [M/F]: ').strip().capitalize()
while sex[0] not in 'FM':
    sex = input('Para de inventar sexo são só dois, tente de novo [M/F]: ')