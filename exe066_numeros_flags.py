print('=-='*10)
print('    Leitor de Números 2.0')
print('=-='*10)
c = s = 0
while True:
    n = int(input('Digite um número [999 para sair]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram inseridos um total de {c} números.')
print(f'O total de números inseridos é igual a {s}.')