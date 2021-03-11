# Um sorteio de um prêmio feito para usuários do Instagram (Usando meus gatos com usuários)

print('O Prêmio deste sorteio será o novo Iphone 25\nVamos ao sorteio..')

import random
from time import sleep

participantes = ['@Nega', '@Bonequinha', '@Pelotinha', '@Elegante', '@Magrelinha', '@Chinesa', '@Ninoso e Ninosa']

print('SORTEANDO...')
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)

print('O ganhador do sorteio foi: ' + participantes[random.randrange(len(participantes))])
