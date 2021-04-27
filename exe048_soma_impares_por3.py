print('Soma de contagem zoada:')
soma = 0
for c in range(1, 500):
    if c%2==1 and c%3==0:
        soma += c
print('Total de ímpares divisíveis por 3: ', soma)

