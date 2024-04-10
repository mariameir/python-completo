# if   / elif   else  / else
# se   / se não se    / se não

entrada = input("Você quer 'entrar' ou 'sair'? ").lower()

if entrada == 'entrar':
    print('Você escolheu entrar')
elif entrada == 'sair':
    print('Você escolheu sair')
else:
    print('Escolha invalida')
