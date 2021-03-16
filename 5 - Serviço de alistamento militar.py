# Serviço de alistamento militar

from datetime import date
atual = date.today().year

from time import sleep

print('='*80)
print('BEM VINDO AO SERVIÇO DE CONSULTA DE ALISTAMENTO DO SERVIÇO MILITAR BRASILEIRO!')
print('='*80)
sleep(2)


nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
sexo = str(input('Digite seu sexo: '))

print('='*80)
print('O Serviço de alistamento Militar Brasileiro é obrigatório apenas para Homens!'.upper())
print('='*80)
sleep(2)

print('Quem nasceu em {} possui {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você precisa efetuar seu alistamento IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não possui 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento deveria ter sido realizado em {}.'.format(ano))

sleep(2)
print('='*80)
print('Obrigado por se alistar. O Brasil agradece pelos seus serviços!'.upper())
print('='*80)
