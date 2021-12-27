"""
Condições IF, ELIF e ELSE - Aula 10
Operadores Relacionais
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
and e (Os dois tem que ser verdadeiro)
or ou (Basta que um seja verdadeiro)
not não (Ele transforma algo verdadeiro em falso ou ao contrario)
in se está (Ex 'ca' in Jessica) Em outras palavras ca está em Jessica Verdadeiro
not in não está (Ex 'di' in Jessica) Em outras palavras di está em Jessica Falso
"""

numero_1 = int(input("Informe o primeiro número: "))
numero_2 = int(input("Informe o segundo número: "))

if numero_1 > numero_2:
    print(f'O mumero maior é {numero_1}')
elif numero_2 == numero_1:
    print(f'O mumero são iguais {numero_2}, {numero_1}')
else:
    print(f'O mumero maior é {numero_2}')

nome = input("Qual seu nome? ")
idade = int(input("qual sua idade? "))
# Limite para pegar empréstimo
idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

if idade_menor < idade and idade < idade_maior:
    print(f'{nome} pode pegar empréstimo')
else:
    print(f'{nome} não pode pegar o empréstimo')

if numero_1 == numero_2 or numero_1 > numero_2:
    print('Verdadeiro')
else:
    print('Falso')

if not(numero_1 == numero_2):
    print('Não é verdadeiro')
else:
    print('É verdadeiro')

if 'ca' in nome:
    print('Existe')
else:
    print('Não existe')

if 'ri' not in nome:
    print('Não existe')
else:
    print('Existe')

usuario = input('Nome de usuário: ')
senha = int(input('Senha do usuario: '))

usuario_db = 'jessica'
senha_db = 123456

if usuario == usuario_db and senha == senha_db:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos')