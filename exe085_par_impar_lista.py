lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n%2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Os valores pares foram: {sorted(lista[0])}')
print(f'Os valores ímpares foram: {sorted(lista[1])}')