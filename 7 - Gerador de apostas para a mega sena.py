from random import randint
from time import sleep

lista = list()
jogos = list()
contador = 0

print('<>'*20)
print(' '*10, ' BOLÃO DA MEGA SENA ', ' '*10)
print('<>'*20)

quantidade = int(input('Quantos bolões deseja fazer? '))
print('AGUARDE...')
sleep(2)

total = 1
while total <= quantidade:
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-'*10, f' SORTEANDO {quantidade} JOGOS ', '-'*10)

for indice, list1 in enumerate(jogos):
    print(f'jogo {indice+1}: {list1}')
    sleep(1)
print('<>'*10)
print('     BOA SORTE     ')
print('<>'*10)
