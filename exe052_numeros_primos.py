print('Números Primos')
n = int(input('Digite o número a ser analizado: '))
# exercício corrigido
print('Os números coloridos são os divísiveis.')
t = 0
for c in range(1, n+1):
    if n%c==0:
        print('\033[31m',end=' ')
        t += 1
        # esse end=' ' serve para que a contagem não mude de linha.
    else:
        print('\033[m', end=' ')
    print('{} '.format(c), end=' ')
if t == 2:
    print('\n\033[m','É primo.')
else:
    print('\n\033[m','Não é primo.')

