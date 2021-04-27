v = float(input('Digite sua velocidae: '))
if v > 80:
    print('Você superou a velocidade máxima! Está multado!')
    print('Valor da multa: R${:.2f}'.format((v-80)*7))
else:
    print('Você está na velocidade adequada, continue assim.')