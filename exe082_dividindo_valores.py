print('Dividindo Valores em Lista')
lista = []
while True:
    n = lista.append(int(input('Digite um número: ')))
    c = str(input('Continuar? [S/N]: '))
    if c in 'SsNn':
        if c in 'Nn':
            break
    else:
        c = str(input('Continuar? [S/N]: '))
par = []
impar = []
for v in lista:
    if v%2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'\nOs resultados foram...')
print(f'Valores inseridos: {lista}')
print(f'Valores inseridos pares: {par}')
print(f'Valores inseridos ímpares: {impar}')
