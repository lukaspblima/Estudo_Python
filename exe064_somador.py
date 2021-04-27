x = n = c =0
while x != 999:
    x = int(input('Digite um valor [999 para parar]: '))
    if x != 999:
        n += x
        c += 1
print('Quantidade de adições: {}. Total: {}'.format(n, n))