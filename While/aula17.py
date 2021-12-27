"""
while em Python
utilizado para realizar açoes enquanto
uma condiçao for verdadeira
Requistos: Enteder condições e operadores
"""

a = 0
while a < 10:
    if a == 3:
        a = a + 1
        # continue  # quando ele cai no if ele faz o que tem que ser feito e continua rodando o código logo a baixo
        break       # já aqui ele encerra essa parte do while

    print(a)
    a = a + 1

print('Terminou')

x = 0   # coluna
y = 0   # linha

while x < 10:
    y = 0
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1
    x += 1
print('Acabou!')

yes_or_not = 'sim'
while yes_or_not == 'sim':
    print()
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número!')
        continue
    num1 = int(num1)
    num2 = int(num2)
    # + - / *
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Operador invalido')
    yes_or_not = input('Deseja continuar? (sim/não)')