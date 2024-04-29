"""
Introdução ao try/execept
try -> tentar executar o codigo
execept -> ocorreu algum erro ao executar o codigo
"""

numero = input('vou dobrar o numero que vc digitar: ')

# if numero.isdigit():
#     numero_float = float(numero)
#     print(f'o dobro e {numero} é {numero_float*2:.2f}')
# else:
#     print('Isso não é um numero')

try:
    numero_float = float(numero)
    print('FLOAT: ', numero_float)
    print(f'o dobro e {numero} é {numero_float*2:.2f}')
except:
    print('Isso não é um numero')
    