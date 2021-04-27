km = float(input('Digite a distância da viagem em KM: '))
if km <= 200:
    print('Sua viagem custará R${:.2f}'.format(km*0.50))
else:
    print('Sua viagem custará R${:.2f}'.format(km*0.45))