print('Pesquisa de Sexos')
h = m = o = 0
sexo = -1
outro = []
while sexo != 0:
        print('[1] Homem [2] Mulher [3] Especifique [0] Sair')
        sexo = int(input('Digite o seu sexo: '))
        if sexo == 1:
            h += 1
        elif sexo == 2:
            m += 1
        elif sexo ==3:
            esp = str(input('Especifique: ')).upper().strip()
            outro.append(esp)
            o += 1
        elif sexo > 3:
            print('Opção Inválida! Tente novamente!')
print('Foram computados {} Homens, {} Mulheres e {} Específicos.'.format(h, m, o))
if o > 0:
    inf = str(input('Deseja saber quais foram as entradas específicas? [S/N] ')).upper()
    if inf == 'S':
        for c in range(0, o):
            print(outro[c], end='; ')
