palavras = ('CARINHO', 'PRINCESA', 'AMOR', 'AMIZADE', 'SAUDADE', 'AFAGO', 'APROXIMAÇAO', 'RESPIRAÇAO', 'CONTATO')
for pal in palavras:
    print(f'\nNa palavra "{pal}" temos:... ', end='')
    for letra in pal:
        if letra in 'AEIOU':
            print(f'"{letra}"', end=' ')