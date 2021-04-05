from random import randint
print('por github.com/lukaspblima')
print('='*35)
msg = 'Rolador de dados!'
print('{:^35}'.format(msg))
print('='*35)
L = int(input('Digite a quantidade de lados: '))
qtd = int(input('Digite a quantidade de dados: '))
modv = int(input('Modificador: '))
if qtd > 1:
    dados = []
    c = 0
    result = 0
    if modv > 0:
        while c < qtd:
            dado = randint(1, L)
            dados.append(dado)
            result = result + dado
            c = c + 1
        print('    ... {}d{} + {} = ...'.format(qtd, L, modv))
        print('O resultado foi: {} + {} = {}'.format(dados, modv, (result+modv)))
    else:
        while c < qtd:
            dado  = randint (1, L)
            dados.append(dado)
            c = c+1
        print('O resultado foi: {}d{} = {}'.format(qtd, L, dados))
else:
    if modv > 0:
        n = randint(1, L)
        print('    ... {}d{} + {} = ...'.format(qtd, L, modv))
        print('O resultado foi: {} + {} = {}'.format(n, modv, (n+modv)))
    else:
        print('O resultado foi: {}d{} = {}'.format(qtd, L, randint(1, L)))
print()
input('Aperte ENTER para sair.')
