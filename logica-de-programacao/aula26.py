'''
formatacao basica de estrings
s - string
d - int
f - float
. - <numero de digitos> f
x ou X - Hexadecimal
(caractere) (><^) (quantidade)
> - esquerda
< - direita
^ - centro
sinal - + ou -
Ex.: o> -100, .1f
Conversion flags - !r !s !a
'''

variavel = 'meir'
print(f'{variavel}')
print(f'{variavel:_>10}')
print(f'{variavel:_<10}')
print(f'{variavel:_^10}')
print(f'{123.232342:+,.2f}')
print(f'o hexadecimal de 1500 é {1500:08X}')
