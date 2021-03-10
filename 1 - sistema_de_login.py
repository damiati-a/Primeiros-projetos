# Sistema simples de login feito com Python


usuario = str(input('Digite seu nome de usuario: '))
senha = input('Digite sua senha: ')

if usuario == 'José Maria' and senha == '1234':
    print('Seja Bem vindo Sr(a) {} !'.format(usuario))
else:
    print('<ERROR>\nO nome de usuário ou senha estão inválidos')
    print('Digite novamente seus dados')

