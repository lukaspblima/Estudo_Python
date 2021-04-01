print('Por github.com/lukaspblima')
print('='*35)
print('        Calcule o seu IMC!')
print('='*35)
print('Utilize ponto ao invés de vírgula.')
alt = float(input('Informe a sua altura em Metros: '))
peso = float(input('Informe o seu peso em KG: '))
imc = peso/(alt**2)
print('IMC Ideal: Entre 18.5 e 24.9.')
if imc < 17 :
    print('Seu IMC = {:.1f}. \nVocê está bem abaixo do seu peso ideal, procure aconselhamento médico.'.format(imc))
elif imc < 18.5 and imc > 17 :
    print('Seu IMC = {:.1f}. \nVocê está abaixo do seu peso ideal, consulte um especialista.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC = {:.1f}. \nVocê está no seu peso ideal, parabéns!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC = {:.1f}. \nVocê está acima do seu peso ideal, consulte um especialista.'.format(imc))
elif imc < 30 and imc < 40:
    print('Seu IMC = {:.1f}. \nVocê está muito acima do seu peso ideal, consulte um especialista.'.format(imc))
else:
    print('Seu IMC = {:.1f}. \nVocê está gravemente acima do seu peso ideal, procure ajuda médica!'.format(imc))
