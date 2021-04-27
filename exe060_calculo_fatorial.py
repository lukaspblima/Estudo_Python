print('Calculo Fatorial')
n = int(input('Digite o número a fatorar: '))
c = n-1
fat = n
print('Fatorial de {} = {} x '.format(n, n), end='')
while c >= 1:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '= {}'.format(fat), end=' ')
    fat *= c
    c -= 1

# é possível simplesmente importar "factorial" da biblioteca "math". Ele automaticamente irá calcular como comando.