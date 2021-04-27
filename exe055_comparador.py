print('Comparador de Números')
n = int(input('Digite o número de termos: '))
maior = 0
menor = 0
for t in range(1, n+1):
    num = int(input('Digite o {}º valor: '.format(t))
    if t == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
