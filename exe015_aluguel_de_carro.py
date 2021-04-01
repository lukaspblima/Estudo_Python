print('Descubra o preço a ser pago ao final do aluguel do seu carro.')
# diária = R$60,00 e R$0,15/Km
dia = int(input('Quantidade de dias alugados (R$60/dia): '))
km = float(input('Quantidade de Kms rodados R$0,15/Km): '))
R = (dia*60)+(km*0.15)
print('Valor das diárias: R${:.2f}'.format(dia*60))
print('Valor da quilometragem: R${:.2f}'.format(km*0.15))
print('O valor total a ser pago é de: R${:.2f}'.format(R))
