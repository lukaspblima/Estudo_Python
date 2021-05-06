print(f'{"Maior e Menor em Lista!":^20}')
lista = []
for c in range(1,6):
    lista.append(int(input(f'Digite {c}º número: ')))
print('Os valores digitados foram: ')
for v in lista:
    print(f' {v}...', end='')
print(f'\nO maior valor foi {max(lista)} na posição ', end='')
for c, v in enumerate(lista):
    if v >= max(lista):
        print(f'{c};', end=' ')
print(f'\nO menor valor foi {min(lista)} na posição ', end='')
for c, v in enumerate(lista):
    if v <= min(lista):
        print(f'{c};', end=' ')