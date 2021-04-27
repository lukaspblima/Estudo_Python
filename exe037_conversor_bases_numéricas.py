print('Converta um número para outra base numérica:')
print('[1] para Decimal ==> Binário\n[2] para Decimal ==> Octal')
print('[3] para Binário ==> Decimal\n[4] para Binário ==> Octal')
print('[5] para Octal   ==> Decimal\n[6] para Octal   ==> Binário')
menu = int(input('Digite a opção desejada: '))
print('-=-'*10)
n = int(input('Digite o número: '))
if menu == 1:
    n2 = bin(n)
    print('O número {} em binário é: {}'.format(n, n2[2:]))
elif menu == 2:
    n2 = oct(n)
    print('O número {} em octal é: {}'.format(n, n2[2:]))
elif menu == 3:
    n = bin(n)
    n2 = dec(n)
    print('O número {} em decimal é: {}'.format(n, n2[2:]))
elif menu == 4:
    n = bin(n)
    n2 = oct(n)
    print('O número {} em octal é: {}'.format(n, n2[2:]))
elif menu == 5:
    n = oct(n)
    n2 = dec(n)
    print('O número {} em decimal é: {}'.format(n, n2[2:]))
elif menu == 6:
    n = oct(n)
    n2 = bin(n)
    print('O número {} em binário é: {}'.format(n, n2[2:]))
else:
    print('Opção Inválida. Tente novamente.')
