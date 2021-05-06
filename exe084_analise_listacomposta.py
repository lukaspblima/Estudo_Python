lista = []
dado = []
maipeso = menpeso = 0
while True:
    nome = str(input('Nome: '))
    dado.append(nome)
    peso = float(input('Peso (Kg): '))
    if len(lista) == 0:
        maipeso = menpeso = peso
    else:
        if peso > maipeso:
            maipeso = peso
        if peso < menpeso:
            menpeso = peso
    dado.append(peso)
    lista.append(dado[:])
    dado.clear()
    resp = str(input('Continuar? [S/N]: '))
    if resp in 'SsNn':
        if resp in 'Nn':
            break
    else:
        resp = str(input('Continuar? [S/N]: '))
print(f'Total de cadastros: {len(lista)}')
print(f'O maior peso foi {maipeso}Kg, referente à: ', end='')
for p in lista:
    if p[1] == maipeso:
        print(p[0], end='; ')
print(f'\nO menor preso foi {menpeso}Kg, referente à: ', end='')
for p in lista:
    if p[1] == menpeso:
        print(p[0], end='; ')
