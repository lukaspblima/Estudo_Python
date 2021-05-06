num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número de 0 a 20: '))
while n > len(num) or n*-1 > len(num):
    n = int(input('Tente novamente. Digite um número de 0 a 20: '))
if n > 0:
    print(f'Você digitou o número "{num[n]}"!')
else:
    print(f'Você digitou o número "menos {num[n*-1]}"!')