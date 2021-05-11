ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break
print('-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)

for indice, alinhar in enumerate(ficha):
    print(f'{indice:<4}{alinhar[0]:<10}{alinhar[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno?(999 interrompe a seção)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< Obrigado >>>')

