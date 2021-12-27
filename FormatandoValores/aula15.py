"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÙMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^- Centro
"""
num_1 = 12
num_2 = 3
divisao = num_1 / num_2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'Ayla Miller'
print(f'{nome:s}')
print(f'{num_2:0<10}')
print(f'{num_2:0>10}')
print(f'{num_1:0^10}')

print(f'{nome:*^20}')

print(nome.lower())     # tudo minusculo
print(nome.upper())     # tudo maiusculo
print(nome.title())     # Primeiras letras maiusculas