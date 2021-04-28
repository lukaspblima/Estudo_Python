tit = 'Tabuada 3.0'
print('=-='*13)
print(f'== {tit:^33} ==')
print('=-='*13)
t = 1
while True:
    n = int(input(f'Insira o {t}º valor [negativo encerar]: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'->  {n} x {c} = {n*c}')
    t += 1
    print('=-='*13)
print('=-='*13)
print('  Programa Encerrado. Volte sempre!')