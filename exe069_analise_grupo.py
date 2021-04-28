print('Analisador de Grupos')
print('--------------------')
t_homem = min_outros = mai_mulher = 0
while True:
    sexo = int(input('Digite [1] Homem [2] Mulher [3] Não Binário: '))
    idade = int(input('Digite sua idade: '))
    if sexo == 1:
        t_homem += 1
    if sexo == 3 and idade > 18:
        min_outros += 1
    if sexo == 2 and idade < 20:
        mai_mulher += 1
    c = str(input('Deseja continuar? [S/N]: '))
    if c in 'Nn':
        break
print(f'Foram cadastrados {t_homem} homem(s).')
print(f'Foram cadastrados {min_outros} não binários maiores de idade.')
print(f'Foram cadastrados {mai_mulher} mulher(es) acima dos 20 anos.')