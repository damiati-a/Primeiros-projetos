# Par ou Ímpar

from random import randint
from time import sleep

v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar?[P/I] ')).strip().upper()[0]
        print('--- PAR OU ÍMPAR ---')
        sleep(2)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    print('DEU PAR!'if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!!!')
            v += 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!!!')
            v += 1
        else:
            print('VOCÊ PERDEU')
    print('Vamos jogar novamente...')
sleep(2)
print(f'Você venceu {v} vezes')