p = float(input('Digite o preço do produto: '))
print('[1] para pagamento a vista em dinheiro.\n[2] para pagamento a vista no cartão.\n[3] para parcelamento no cartão.')
c = int(input('Digite a opção para a condição de pagamento: '))
vista = p-(p*0.1)
vcar = p-(p*0.05)
if c == 1:
    print('O valor a ser pago é de R${:.2f}'.format(vista))
elif c == 2:
    print('O valor a ser pago é de R${:.2f}'.format(vcar))
elif c == 3:
    n = int(input('Digite a quantidade de parcelas: '))
    if n == 2:
        print('O valor a ser pago é de R${:.2f}'.format(p))
    elif n > 2:
        v = p+(p*0.2)
        print('O valor a ser pago é de R${:.2f} em {} de R${:.2f}.'.format(v, n, v/n))
