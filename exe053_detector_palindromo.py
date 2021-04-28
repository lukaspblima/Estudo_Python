print('Detector de Palindromos')
p = input('Digite uma palavra: ').upper().split()
p = ''.join(p)
"""inv = ''
for c in range(len(p)-1, -1, -1):
    inv += p[c]"""
inv = p[::-1] # macete utilizando fatiamento de strings
if inv == p:
    print('É um palindromo.')
else:
    print('Não é um palindromo.')
