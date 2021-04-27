s_idade = 0
maiorid_h = 0
nome_maiorid_h = ''
maiorid_m = 0
nome_maiorid_m = ''
maiorid_o = 0
nome_maiorid_o = ''
menoridade = 0

print('=='*15)
print('==  {}ANALISADOR DE PESSOAS{}  =='.format('\033[33m', '\033[m'))
print('=='*15)
indice = int(input('Digite o número de entradas: '))
for c in range(1, indice+1):
    print('----      {}{}ª PESSOA{}      ----'.format('\033[33m', c, '\033[m'))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/H/O]: ')).strip().upper()
    s_idade += idade
    if idade < 21:
        menoridade += 1
    if indice == 1:
        if sexo == 'H':
            maiorid_h += idade
            nome_maiorid_h = nome
        elif sexo == 'M':
            maiorid_m += idade
            nome_maiorid_m = nome
        else:
            maiorid_o += idade
            nome_maiorid_o = nome
    if sexo == 'H' and idade > maiorid_h:
        maiorid_h = idade
        nome_maiorid_h = nome
    if sexo == 'M' and idade > maiorid_m:
        maiorid_m = idade
        nome_maiorid_m = nome
    if sexo == 'O' and idade > maiorid_o:
        maiorid_o = idade
        nome_maiorid_o = nome

media_idade = s_idade // indice
print('{}*{} A idade média do grupo é de {} anos.'.format('\033[31m', '\033[m', media_idade))
print('{}**{} Há um total de {} pessoa(s) menor(es) de idade.'.format('\033[31m', '\033[m', menoridade))
print('{}***{} O homem mais velho é {}, com {} anos.'.format('\033[31m', '\033[m', nome_maiorid_h, maiorid_h))
print('{}***{} A mulher mais velha é {}, com {} anos.'.format('\033[31m', '\033[m', nome_maiorid_m, maiorid_m))
print('{}***{} A pessoa não binária mais velha é {}, com {} anos.'.format('\033[31m', '\033[m', nome_maiorid_o, maiorid_o))
