matriz = [[], [], []]
somapar = somac3 = mail2 = 0
for c in range(1, 10):
    n = int(input(f'Digite o {c}º número: '))
    if n%2 == 0:
        somapar += n
    if c < 4:
        matriz[0].append(n)
    elif c > 3 and c < 7:
        matriz[1].append(n)
    else:
        matriz[2].append(n)
for a in range(0, 3):
    somac3 += matriz[a][2]
    for b in range(0, 3):
        print(f'[ {matriz[a][b]:^5} ]', end=' ')
        if matriz[1][b] > mail2:
            mail2 = matriz[1][b]
    print()
print(f'A soma dos valores pares é: {somapar}')
print(f'A soma dos valores da terceira coluna é: {somac3}')
print(f'A soma dos valores pares é: {mail2}')