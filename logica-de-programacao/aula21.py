# and

entrada = input('[E] Entrar [S]Sair ').lower
senha = input('Digite sua senha: ')
senha_correta = '123456'

if entrada == 'E' and senha == senha_correta:
    print('Entrando')
else: 
    print('Saindo')
