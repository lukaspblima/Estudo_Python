vcasa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o valor do seu salário: R$'))
pre = int(input('Digite o número de prestações: '))
parc = float(vcasa/pre)
if parc <= sal*0.3 :
    print('Empréstimo {}aprovado!{} A mensalidade será de: R${:.2f}'.format('\033[34m', '\033[m]', parc))
else:
    print('Empréstimo {}negado!{} A mensalidade de R${:.2f} supera 30% do seu salário.'.format('\033[31m', '\033[m', parc))