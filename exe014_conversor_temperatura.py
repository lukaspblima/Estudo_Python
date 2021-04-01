# celsius -> fahrenheit
print('='*26)
print('Conversor de Temperaturas: \n[1] Celsius para Fahrenheit. \n[2] Fahrenheit para Celsius.')
print('='*26)
tipo = input('Digite a conversão desejada [1]/[2]: ')
if tipo == '1' :
    C = float(input('Digite a temperatura em Celsius a ser convertida: '))
    tempF= 9*C/5+32
    print('Resultado: {}°C é igual a {:.1f}°F.'.format(C, tempF))
else:
    F = float(input('Digite a temperatura em Fahrenheit a ser convertida: '))
    tempC= ((F-32)*5)/9
    print('Resultado: {}°F é igual a {:.1f}°C.'.format(F, tempC))