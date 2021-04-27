q = t = maior = menor = 0
c = ''
while c != 'N':
    n = int(input('Digite um valor: '))
    q += 1
    t += n
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    c = str(input('Continuar? [S/N]: ')).strip().upper()
print('Média: {}'.format(t/q))
print('Maior Valor: {}\nMenor Valor: {}'.format(maior, menor))