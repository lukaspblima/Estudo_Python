print('Lista de Valores Únicos')
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado! Não será adicionado.')
    c = str(input('Deseja continuar? [S/N]: '))
    if c in 'SsNn':
        if c in 'Nn':
            break
    else:
        c = str(input('Deseja continuar? [S/N]: '))
print(f'Os valores digitados foram: {sort(lista)}')