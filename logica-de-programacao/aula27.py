"""
Fatiamento de strings
12345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i - inicio
f - fim
p - passo (de quantos e quantos caracteres ele vai pular)
Obs.: a funcao len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
print(len(variavel))
print(variavel[4])
print(variavel[4:])
print(variavel[0:9:2])
print(variavel[-1:-10:-1])
print(variavel[::-1])
