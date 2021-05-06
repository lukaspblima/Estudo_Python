turma = []
print(f'{"BOLETIM ESCOLAR":^30}')
print(f'{"=-="*10}')
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2 ) / 2
    turma.append([nome, n1, n2, media])
    c = str(input('Continuar? [S/N]: '))
    if c in 'NnSs':
        if c in 'Nn':
            break
    else:
        c = str(input('Continuar? [S/N]: '))
    print('--------------')
print(f'{"=-="*10}')
print(f'Nº.  {"NOME":<18} MÉDIA   ')
print('-------------------------------')
for t in range(0, len(turma)):
    print(f'{t}    {turma[t][0]:<18} {turma[t][3]:.1f}')
q = str(input('Checar notas? [S/N]: '))
print('-------------------------------')
if q in 'Ss':
    while True:
        a = int(input('Digite o nº do aluno (999 para sair): '))
        if a == 999:
            break
        print(f'As notas de {turma[a][0]} foram: ', end='')
        for x in range(1, 3):
            print(f'[{turma[a][x]}] ', end='')
        print('\n--------------')
print('<<< FIM DA EXECUÇÂO >>>')