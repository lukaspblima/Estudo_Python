print('='*38)
print('{:^38}'.format(' SIMULADOR CAIXA ELETRÔNICO '))
print('='*38)
saque = int(input('Insira o valor a ser sacado: R$'))
totalnota = 0
notas = [100, 50, 20, 10, 5, 1]
for c in range(0, 6):
    if saque > 0:
        totalnota = saque // notas[c]
        if totalnota > 0:
            print(f'Total de {totalnota} notas de {notas[c]}')
            saque = saque%notas[c]
print('='*38)
print('OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS!')

