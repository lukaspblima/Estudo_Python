sal = float(input('Digite o valor do seu salário: R$'))
if sal < 1250:
    print('Seu novo salário é: R${:.2f}'.format(sal+(sal*0.15)))
else:
    print('Seu novo salário é: R${:.2f}'.format(sal + (sal * 0.10)))